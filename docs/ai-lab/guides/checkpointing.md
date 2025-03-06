
On AI-LAB, jobs are limited to a maximum runtime of 12 hours. Once this time limit is reached, your job will be canceled, and any unsaved data will be lost. To prevent data loss, it’s important to implement checkpointing, which saves data at regular intervals. Additionally, you can set up automatic requeuing so that your job will restart automatically if it gets canceled, removing the need to manually resubmit it.

This guide explains how to set up checkpointing in various frameworks like Python, PyTorch, and TensorFlow, as well as how to configure automatic requeuing for your jobs.

!!! info "Disclaimer"
    Using checkpointing is done at your own risk. This guide is intended as a reference, but saving data via checkpointing is entirely the responsibility of the user. There may be errors or inaccuracies within this guide. If you encounter any issues or discover mistakes, we encourage you to provide feedback so we can improve. You can submit your feedback [here](https://serviceportal.aau.dk/serviceportal?id=sc_cat_item&sys_id=a05e2fb4c3434610f0f3041ad001310e).

### Checkpointing methods

Checkpointing allows you to periodically save the state of your job so that it can be resumed later, even after an interruption. Different frameworks have different methods for implementing checkpointing. Below are examples for Python, PyTorch, and TensorFlow. 

??? python "Python checkpointing"

    In Python, you can use the [pickle](https://docs.python.org/3/library/pickle.html) module to periodically save and load the state of your job.

    ``` py linenums="1"
    import pickle
    import os

    def save_checkpoint(data, filename):
        """Save the checkpoint data to a file."""
        with open(filename, 'wb') as f:
            pickle.dump(data, f)

    def load_checkpoint(filename):
        """Load the checkpoint data from a file."""
        with open(filename, 'rb') as f:
            return pickle.load(f)

    # Check if there is a checkpoint file
    if os.path.exists('checkpoint.pkl'):
        # If there is, load the checkpoint
        data = load_checkpoint('checkpoint.pkl')
        print("Resuming from checkpoint:")
    else:
        # If there isn't, initialize data
        data = {'counter': 0}

    try:
        # Simulate some long-running process
        while True:
            data['counter'] += 1
            print("Current counter value:", data['counter'])
            # Save checkpoint every 5 iterations
            if data['counter'] % 5 == 0:
                save_checkpoint(data, 'checkpoint.pkl')
            # Simulate some work
            # Replace this with your actual process
            import time
            time.sleep(1)
    except KeyboardInterrupt:
        # Save checkpoint if the process is interrupted
        save_checkpoint(data, 'checkpoint.pkl')
        print("\nCheckpoint saved. Exiting...")
    ```
    <br>

    #### Breakdown of the key components:

    First, the script checks if a checkpoint file named `checkpoint.pkl` exists using `os.path.exists()`. If the file exists, it loads the checkpoint data using `load_checkpoint` function and assigns it to data. If not, it initializes data with a dictionary containing a single key `counter` initialized to 0. 

    Then, it enters an infinite loop (simulating a long-running process), where it increments the `counter` key of the data dictionary, prints the current counter value, and simulates some work (in this case, a 1-second delay using `time.sleep(1)`).

    Every 5 iterations (`if data['counter'] % 5 == 0)`, it saves the checkpoint by calling `save_checkpoint`. If the process is interrupted by a keyboard interrupt (Ctrl+C), it saves the current checkpoint and prints a message before exiting.

??? pytorch "PyTorch checkpointing"

    PyTorch provides native support for saving and loading model and optimizer states during training. More information about PyTorch checkpointing can be found [here](https://pytorch.org/tutorials/recipes/recipes/saving_and_loading_a_general_checkpoint.html). Here's an example that shows how to checkpoint during training of a simple neural network:


    ``` py linenums="1" hl_lines="39 40 41 46 47 48 49 50 51 52 53 54 55 69 70 71 72 73 74 75"
    import os
    import torch
    import torch.nn as nn
    import torch.optim as optim
    from torchvision import datasets, transforms

    # Define a simple feedforward neural network
    class SimpleNN(nn.Module):
        def __init__(self):
            super(SimpleNN, self).__init__()
            self.fc1 = nn.Linear(784, 512)
            self.relu = nn.ReLU()
            self.dropout = nn.Dropout(0.2)
            self.fc2 = nn.Linear(512, 10)

        def forward(self, x):
            x = self.fc1(x)
            x = self.relu(x)
            x = self.dropout(x)
            x = self.fc2(x)
            return x

    # Load MNIST dataset
    train_loader = torch.utils.data.DataLoader(
        datasets.MNIST('data', train=True, download=True,
                    transform=transforms.Compose([
                        transforms.ToTensor(),
                        transforms.Normalize((0.1307,), (0.3081,))
                    ])),
        batch_size=64, shuffle=True)

    # Define the model
    model = SimpleNN()

    # Define the optimizer and loss function
    optimizer = optim.Adam(model.parameters())
    criterion = nn.CrossEntropyLoss()

    # Checkpoint directory
    checkpoint_dir = 'checkpoints'
    os.makedirs(checkpoint_dir, exist_ok=True)

    ##epoch number of steps
    epoch_steps = 20

    # Check if there are existing checkpoints
    if os.listdir(checkpoint_dir):
        # If there are existing checkpoints, load the latest one
        latest_checkpoint = max([int(file.split('.')[0]) for file in os.listdir(checkpoint_dir)])
        checkpoint = torch.load(os.path.join(checkpoint_dir, f'{latest_checkpoint}.pt'))
        model.load_state_dict(checkpoint['model_state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        start_epoch = latest_checkpoint + 1
    else:
        start_epoch = 0

    # Training loop
    for epoch in range(start_epoch, epoch_steps):
        for batch_idx, (data, target) in enumerate(train_loader):
            optimizer.zero_grad()
            data = data.view(data.size(0), -1)
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()

        print(f'Epoch {epoch}: Loss {loss.item()}')

        # Save checkpoint every epoch
        torch.save({
            'epoch': epoch,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'loss': loss
            }, os.path.join(checkpoint_dir, f'{epoch}.pt'))
    ```

    <br>

    #### Breakdown of the key components:

    <span style="font-weight:700;">Checkpoint Directory Setup (line 39-41):</span> Creating a directory for storing checkpoints.

    <span style="font-weight:700;">Checking for Existing Checkpoints (line 46-55):</span> Checking for existing checkpoints and loading the latest one if available.

    <span style="font-weight:700;">Saving Checkpoints (line 69-75):</span> Saving the model's state, optimizer's state, and current loss at the end of each epoch to a uniquely named file based on the epoch number.


??? tensorflow "TensorFlow checkpointing"

    TensorFlow offers built-in functionality for saving model weights during training using the `ModelCheckpoint` callback. More information about TensorFlow checkpointing can be found [here](https://www.tensorflow.org/tutorials/keras/save_and_load). Here's an example:


    ``` py linenums="1" hl_lines="37 38 39 41 42 43 44 45 46 48 49 50 51 52 53 59 60 61 62 63 64 67 68 75"
        import os
        import sys
        import os.path
        import tensorflow as tf
        from tensorflow import keras

        #####Get an example dataset - we'll use the MNIST dataset first 1000 examples:
        (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

        train_labels = train_labels[:5000]
        test_labels = test_labels[:5000]

        train_images = train_images[:5000].reshape(-1, 28 * 28) / 255.0
        test_images = test_images[:5000].reshape(-1, 28 * 28) / 255.0

        ##epoch number of steps for each job:
        epoch_steps=20

        ####Define a simple sequential model:
        def create_model():
            model = tf.keras.models.Sequential([
                keras.layers.Dense(512, activation='relu', input_shape=(784,)),
                keras.layers.Dropout(0.2),
                keras.layers.Dense(10)
            ])

            model.compile(optimizer='adam',
                            loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
                            metrics=[tf.metrics.SparseCategoricalAccuracy()])

            return model


        # Create a new model instance
        model = create_model()

        # Include the epoch in the file name (uses `str.format`)
        checkpoint_path = "checkpoints/{epoch:d}.ckpt"
        checkpoint_dir = os.path.dirname(checkpoint_path)

        # Create a callback that saves the model's weights every epoch (period=1)
        cp_callback = tf.keras.callbacks.ModelCheckpoint(
            filepath=checkpoint_path, 
            verbose=1, 
            save_weights_only=True,
            period=1)

        # Check if there are existing checkpoints
        if os.path.exists(checkpoint_dir):
            # If there are existing checkpoints, load the latest one
            latest = tf.train.latest_checkpoint(checkpoint_dir)
            # Load the previously saved weights, if there are any:
            model.load_weights(latest)

            # Re-evaluate the model
            loss, acc = model.evaluate(test_images,  test_labels, verbose=2)
            print("Restored model, accuracy: {:5.2f}%".format(100*acc))

            # Get the step number from the latest checkpoint
            ckpt = tf.train.get_checkpoint_state(checkpoint_dir) 
            step = int(os.path.basename(ckpt.model_checkpoint_path).split('.')[0])
            print('Continuing calculation from epoch step:' + str(step)) 
            # Set the initial epoch to the last recovered epoch
            initialEpoch=step
        else:
            initialEpoch=0
            # Save the weights for the initial epoch
            model.save_weights(checkpoint_path.format(epoch=0))

        # Train the model with the new callback
        model.fit(train_images, 
                train_labels,
                epochs=epoch_steps, 
                initial_epoch=initialEpoch,
                callbacks=[cp_callback],
                validation_data=(test_images,test_labels),
                verbose=1)
    ```

    <br>

    #### Breakdown of the key components:

    <span style="font-weight:700;">`checkpoint_path`:</span> Specify the path where checkpoints will be saved. You can include dynamic elements such as epoch number in the file name to differentiate between checkpoints, like `checkpoints/{epoch:d}.ckpt`

    <span style="font-weight:700;">`cp_callback`:</span> Create a ModelCheckpoint callback, which will save the model's weights at specified intervals during training. You can customize various parameters such as the file path, verbosity, and whether to save only the weights or the entire model.

    <span style="font-weight:700;">`model.load_weights(latest)`:</span> Before starting training, check if there are existing checkpoints. If so, load the latest one to resume training from the last saved state. This ensures continuity in training even if interrupted.

