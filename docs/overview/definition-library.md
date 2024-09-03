## Computing definitions
???+ news "HPC (High Performance Computing)"
    High-performance computing (HPC) involves the use of powerful computing resources to perform computationally demanding tasks that are beyond the capability of traditional computing systems. HPC is used to process large datasets, perform simulations, and run resource-intensive applications, such as modelling climate patterns, simulating molecular behaviour, analysing genetic data, designing and testing products and structures, simulating fluid dynamics, optimizing manufacturing processes, identifying trends, and making predictions. HPC allows processing and analysis of complex data, leading to faster discoveries, more efficient processes, and better decision-making.

??? news "Cloud computing"
    All the HPC systems presented on the HPC Matchmaker are systems accessible in the cloud. Cloud computing refers to on-demand delivery and access to computing resources -like applications, servers, or storage - via the Internet. This way the user can access the resources through their local machine from any location, which results in high accessibility and convenience of use. In the context of data analysis, cloud services allow users to perform high-demanding computational tasks in a relatively short time.

??? news "Parallel processing"
    Parallel processing is the technique of dividing a single task into smaller parts that can be executed simultaneously on multiple processors or computing systems. It is often used in HPC to speed up computations and increase efficiency. The hardware component crucial for enabling parallel processing is GPU.

??? news "Virtual machine (VM)"
    A virtual machine (VM) is a software environment that emulates a physical computer, including hardware components such as a CPU, memory, and storage. VMs are commonly used in HPC to create isolated environments for running scientific applications, providing users with the flexibility to customize and configure the environment to their specific needs without interfering with other users or applications running on the same hardware.

## Hardware components definitions
??? news "Central Processing Unit (CPU)"
    The Central Processing Unit - CPU - is the primary component of a computer that performs arithmetic, logic, and input/output operations. It is often referred to as the 'brain' of the computer. HPC systems typically use multiple CPUs or multicore processors to perform large-scale calculations in parallel, allowing for much faster processing of data and computation than can be achieved with a single CPU.

??? news "Graphics Processing Unit (GPU)"
    The GPU (Graphics Processing Unit) is a specialized processor optimized for parallelizable tasks, such as image processing, scientific simulations, and machine learning. Unlike a CPU, which is optimized for single-threaded performance, a GPU can perform many computations simultaneously, making it ideal for the large-scale data processing needed in HPC. GPUs can be used alone or with CPUs to accelerate specific calculations, and many HPC systems have numerous GPUs to achieve maximum computational power.

??? news "HPC Memory"
    Memory in high-performance computing plays a great role in providing fast and temporary storage of data to support data-intensive tasks. Memory stores the currently processed data in the system, which is especially important for simultaneous tasks run in parallel, where holding extensive and large data sets it's crucial and very important.

??? news "HPC Storage"
    While storage on a regular local machine means long-term saving the data in the local drive for easy and fast access to it, the storage systems in HPC are slightly different. Since high-performance computing allows performing multiple tasks in parallel, the role of storage is to provide a vast I/O (input/output) to be able to scale out with the compute and enable the CPUs to 'work', while not overloading with data.

## Computing infrastructure definitions
??? news "Cluster"
    A cluster is a group of computers that are connected to work as a single system. It is often used in HPC to distribute workloads across multiple systems to increase performance and processing power.

??? news "Node"
    In the context of a cluster, a node is a single computer within the cluster that performs computations and communicates with other nodes in the cluster.

??? news "Front-end node"
    The front-end node is used for logging into the platform, accessing your files, and starting jobs on the compute nodes. The front-end node is a relatively small server which is not meant for performing heavy computations; only light-weight operations such as transferring files to and from AI-LAB and defining and launching job scripts.

## System environment definitions
??? news "Command-line"
    The command-line is a text-based interface used to interact with a computer system or program. Users enter commands and parameters to execute operations, typically without the use of a graphical user interface.

??? news "Graphical User Interface (GUI)"
    GUI (Graphical User Interface) is a type of user interface that uses visual representations of controls and elements to interact with a computer program or system. It allows users to interact with software in a more intuitive and user-friendly way compared to command-line interfaces.

??? news "Linux"
    All HPC resources available through Aalborg University use Linux. Linux is a popular open-source operating system based on the Unix operating system. It is widely used in HPC environments due to its flexibility, performance, and ability to be customized for specific use cases.

??? news "Slurm"
    Slurm is a management and job-scheduling queue system, which is used for Linux clusters. It requires users to specify commands and resources needed to run the job. Then, Slurm prioritizes the job according to prompted tasks and the resource availability, and adds the job to the queue, among other user's requests. Slurm is utilized in AI Cloud HPC.

??? news "Containerisation"
    Containerisation refers to the process of creating isolated software environments that contain all the necessary dependencies and configurations needed to run an application. Containers provide a lightweight and portable solution for deploying applications across different HPC systems without the need to modify the underlying operating system. This makes it easier to share and reproduce software environments and enables more efficient use of HPC resources by allowing multiple applications to run on the same node without interfering with each other.

## Data classification definitions
??? news "Data Classification Model"
    There are certain limitations to each of the HPC resources available through Aalborg University regarding the data levels which can be managed on them. Data Classification Model consist of predefined categories of data which determine how the data should be accessed and treated by those who handle it.

??? news "Data level 0: Public information"
    Information which is in the public domain, and where disclosure is not harmful to AAU.

??? news "Data level 1: internal information"
    The information which only users with a purely work-related need may and can have access to, and where a breach of confidentiality will have no or a low impact on AAU, private individuals, or partner(s).

??? news "Data level 2: confidential information"
    The information which only users with a purely work-related need may and can have access to, and where a breach of confidentiality will have semi-serious impacts for AAU, private individuals, or partner(s).

??? news "Data level 3: sensitive information"
    This is information which, by virtue of its personal, technical, commercial, or competitive nature and sensitivity, must be protected against unintentional access and disclosure.