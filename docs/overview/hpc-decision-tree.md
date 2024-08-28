<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>

<style>
    .content {
        width: 80vw;
        max-width: 900px;
        min-width: 300px;
        margin: 20px;
        border-radius: 20px;
        background-color: white;
        padding: 40px;
    }
    p {
        font-size: 16px;
        font-weight: 400;
        color: #404f5f;
        margin-top: 1rem;
        font-family: Roboto, sans-serif;
    }
    a {
        text-decoration: none;
        color: rgb(44, 47, 52);
    }
    span {
        font-family: Roboto, sans-serif;
    }
    h1 {
        color: #211a52;
        font-size: 34px;
        font-weight: 600;
        font-family: Roboto, sans-serif;
        margin-bottom: 0rem;
    }
    h2 {
        color: #211a52;
        font-size: 24px;
        font-weight: 600;
        white-space: normal;
        margin-top: 40px;
        font-family: Roboto, sans-serif;
    }
    h3 {
        color: #211a52;
        font-size: 18px;
        font-weight: 500;
        margin-bottom: 30px;
        font-family: Roboto, sans-serif;
    }
    h4 {
        color: #0f0c09;
        font-size: 18px;
        font-weight: 600;
        margin: 0;
        font-family: Roboto, sans-serif;
    }
    h5 {
        color: #211a52;
        font-size: 16px;
        font-weight: 500;
        margin-bottom: 0rem;
        font-family: Roboto, sans-serif;
    }
    .claaudia-text {
        padding-left: 10px;
        margin-top: 10px;
    }
    .remaining-progress {
        border-radius: 20px !important;
        height: 25px;
        margin-right: 20px;
        width: 100%;
    }
    #remaining-progress-bar {
        background-color: #6200EE !important;
        color: #fff;
        font-size: 16px;
        font-weight: 500;
        font-family: Roboto, sans-serif;
    }
    .quiz-body {
        display: flex;
        justify-content: space-between;
        height: 500px;
    }
    .sections-container {
        display: flex;
        width: 100%;
    }
    .survey {
        flex-grow: 1;
        padding-right: 10px;
    }
    .question-content {
        margin-block: 1rem 2rem;
    }
    .form-check {
        border: 2px solid #d5d8dc;
        border-radius: 8px;
        margin-bottom: 1.5rem;
        padding-left: 3rem;
        padding-right: 2rem;
        transition: all .15s ease-in-out;
        cursor: pointer;
        display: flex;
        align-items: center;
    }
    .form-check.question-option.selected {
        border-color: #6200EE;
    }
    .question-option:hover {
        background-color: #fafafa;
    }
    .question-option-content {
        align-items: center;
        display: flex;
        gap: 8px;
        position: relative;
        vertical-align: top;
        font-size: 16px;
        font-weight: 400;
        font-family: Roboto, sans-serif;
    }
    .form-check-label {
        height: 100%;
        width: 100%;
        align-content: center;
        padding-left: 20px;
        color: #211a52;
        font-weight: 400;
        font-family: Roboto, sans-serif;
        font-size: 16px;
        min-height: 50px;
        padding-top: 3px;
        padding-bottom: 3x;
    }
    .form-check-input {
        margin-top: 0 !important;
    }
    .form-check-input:checked {
        background-color: #6200EE;
        border-color: #6200EE;
    }

    .next-btn, .next-previous {
        align-items: center;
        display: flex;
        flex-direction: row;
        background-color: #6200EE;
        padding: 0.5rem 1.8rem;
        transition: all .15s ease-in-out;
        cursor: pointer;
        border-radius: 4px;
        color: #fff;
        font-family: Roboto, sans-serif;
        font-size: 16px;
        font-weight: 600;
        text-align: center;
    }
    .next-btn:hover {
        background-color: #3700B3;
    }
    .next-previous {
        color: #54616e !important;
        background-color: transparent !important;
        padding-top: 0.5rem;
        padding-bottom: 0.5rem;
        padding-right: 1.8rem;
        padding-left: 0.5rem;
    }
    .button-container {
        display: flex;
        flex-direction: column;
        height: 40px;
    }
    .button-content .next-btn[style*="display: none"] ~ .next-previous {
        margin-right: auto;
    }
    .button-content .next-previous[style*="display: none"] ~ .next-btn {
        margin-left: auto;
    }
    .button-content {
        padding: 0;
        display: flex;
        justify-content: space-between;
        margin-left: 0;
        margin-right: 0;
        flex-wrap: wrap;
        gap: 16px;
    }
    .survey-tooltip {
        background-color: #ebebef;
        border-radius: 50%;
        height: 15px;
        position: relative;
        transition: all .15s ease-in-out;
        width: 15px;
    }
    .survey-tooltip:hover {
        background-color: #211a52;
        cursor: pointer;
    }
    .survey-tooltip span {
        color: #211a52;
        font-size: 12px;
        font-weight: 600;
        left: 50%;
        position: absolute;
        top: 50%;
        -webkit-transform: translate(-50%, -50%);
        transform: translate(-50%, -50%);
        transition: all .15s ease-in-out;
    }
    .survey-tooltip:hover span {
        color: #fff;
    }
    .survey-tooltip:hover .tooltip-text {
        visibility: visible;
    }
    .tooltip-text {
        border-radius: 4px;
        bottom: 2rem;
        color: #fff;
        font-size: 14px;
        font-weight: 400;
        left: -2rem;
        max-width: 350px;
        padding: 1rem;
        visibility: hidden;
        white-space: normal;
        width: -webkit-max-content;
        width: max-content;
        font-family: Roboto, sans-serif;
        z-index: 1;
    }
    .tooltip-text, .tooltip-text:before {
        background-color: #211a52;
        position: absolute;
    }
    .tooltip-text:before {
        bottom: -2.5%;
        content: "";
        left: 6.5%;
        padding: 6px;
        -webkit-transform: rotate(45deg);
        transform: rotate(45deg);
        z-index: -1;
    }
    .finished {
        display: none;
    }
    .retake-quiz-button {
        align-items: center;
        background-color: transparent;
        display: flex;
        gap: 1rem;
        transition: all .15s ease-in-out;
        color: #6200EE;
        font-size: 16px;
        font-weight: 400;
        text-decoration: none;
        border: none;
        cursor: pointer;
        font-family: Roboto, sans-serif;
    }
    .retake-quiz-button .left-arrow {
        fill: #6200EE;
        -webkit-transform: translateX(0);
        transform: translateX(0);
        transition: all .15s ease-in-out;
    }
    .retake-quiz-button:hover {
        color: #3a2faa;
        cursor: pointer;
    }
    .retake-quiz-button:hover .left-arrow {
        fill: #3a2faa;
        -webkit-transform: translateX(-.5rem);
        transform: translateX(-.5rem);
    }
    .go-to-hpc-btn {
        background-color: #6200EE;
        border-radius: 4px;
        padding: 0.8rem 1.5rem;
        transition: all .15s ease-in-out;
        color: white !important;
        font-size: 14px;
        font-weight: 500;
        font-family: Roboto, sans-serif;
        text-decoration: none;
    }
    .go-to-hpc-btn:hover {
        background-color: #3700B3;
        cursor: pointer;
    }
    .divider-horizontal {
        background-color: #ebebef;
        height: 1px;
        width: 100%;
    }
    .reset-btn {
        background-color: transparent;
        border: 1px solid #d5d8dc;
        border-radius: 4px;
        height: -webkit-max-content;
        height: max-content;
        padding: 5px 10px;
        transition: all .15s ease-in-out;
        text-decoration: none;
        cursor: pointer;
        display: inline-block;
        color: #211a52;
        font-family: Roboto, sans-serif;
        font-size: 13.3333px;
    }
    .reset-btn:hover {
        background-color: #fafafa;
        cursor: pointer;
    }
    .spec {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .spec-content {
        padding: 3rem 3rem;
        margin-top: 20px;
        background: whitesmoke;
        border-radius: 10px;
    }
    .spec-content-body {
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        margin-bottom: 20px;
    }
    .option-item {
        padding-top: .5rem;
    }
    .option-item-title {
        color: #211a52;
        font-size: 13px;
        font-weight: 600;
        font-family: Roboto, sans-serif;
    }
    .option-item-item {
        align-items: center;
        display: flex;
        gap: 1rem;
        margin-bottom: 1rem;
    }
    .option-item-item-body {
        color: #404f5f;
        font-size: 14px;
        font-weight: 400;
        font-family: Roboto, sans-serif;
        margin: 0;
    }
    #spec-title {
        margin-top: 0;
        align-self: flex-end;
    }
    .spec-content-header {
        margin-bottom: 20px;
    }
    @media (max-width: 920px) {
        .content {
            width: 90vw;
            padding: 30px;
        }
        .quiz-body {
            flex-direction: column;
        }
        .sections-container {
            flex-direction: column;
        }
    }
    @media (max-width: 600px) {
        h1 {
            font-size: 28px;
        }
        h2{
            font-size: 16px;
        }
        .claaudia-text {
            font-size: 12px;
        }
        .content {
            width: 95vw;
            padding: 15px;
            margin: 0;
        }
        .retake-quiz-button {
            margin-bottom: 20px;
        }
        .md-content {
            padding-top: 2rem;
            padding-left: 0;
            padding-right: 0;
            margin-left: 0;
            margin-right: 0;
        }
    }
</style>

<div class="content">
    <div style="display: flex; justify-content: space-between;">
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <h1>HPC Decision Tree</h1>
            <h5 class="claaudia-text">By CLAAUDIA</h5>
        </div>
    </div>
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div class="progress remaining-progress" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">
            <div id="remaining-progress-bar" class="progress-bar" style="width: 0%">0%</div>
        </div>
        <button type="button" id="reset-btn" class="reset-btn">
            <div style="display: flex; align-items: center;">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="15" fill="currentColor" class="bi bi-arrow-clockwise" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 3a5 5 0 1 0 4.546 2.914.5.5 0 0 1 .908-.417A6 6 0 1 1 8 2z"/>
                    <path d="M8 4.466V.534a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384L8.41 4.658A.25.25 0 0 1 8 4.466"/>
                </svg>
                <p style="margin-top: 0 !important; margin-bottom: -2px !important; padding-left: 4px;">Reset</p>
            </div>
        </button>
    </div>

    <div class="quiz-body">
        <div class="sections-container">
            <div class="survey">
                <h2 id="quiz-title"></h2>
                <div id="quiz-title-hint"></div>
                <div class="question-content"></div>
                <div class="button-container">
                    <div class="button-content">
                        <div class="next-previous">Previous</div>
                        <div class="next-btn">Next</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="finished">
        <div class="spec">
            <h4 style="margin-top: 20px;">We recommend the following HPC platform for you:</h4>
            <div class="spec-content">
                <div class="spec-content-header">
                    <div style="display: flex; justify-content: space-between;">
                        <h2 id="spec-title"></h2>
                    </div>
                </div>
                <p id="spec-description"></p>
                <div class="divider-horizontal"></div>
                <div class="spec-content-body">
                    <div class="option-item">
                        <p class="option-item-title">HARDWARE SPECIFICATIONS</p>
                    </div>
                    <div>
                        <div class="option-item">
                            <p class="option-item-title">KEY FEATURES</p>
                        </div>
                    </div>
                    <div>
                        <div class="option-item">
                            <p class="option-item-title">DATA CLASSIFICATION</p>
                        </div>
                        <div class="option-item">
                            <p class="option-item-title">RECOMMENDED SKILLS</p>
                        </div>
                    </div>
                </div>
                <a class="go-to-hpc-btn" href=""></a>
            </div>
        </div>
    </div>
</div>

<script>

    function initializePage() {
        const quizData = [
            {
                hpc: ["AI-LAB", "AI Cloud", "UCloud", "Strato"],
                question: "What is your primary role at AAU in using HPC resources?",
                options: ["Student", "Researcher", "Lecturer"],
                next: [
                    {
                        hpc: ["AI-LAB", "UCloud", "Strato"],
                        question: "Do you need to process or store confidential or sensitive data?",
                        options: ["I'm only working on data levels 0, 1<span><div class='survey-tooltip'><span>?</span><p class='tooltip-text'>Data level 0: Public information. Data level 1: Internal information - only users with a purely work-related need may and can have access to.</p></div></span>", "I will include data levels 2, 3<span><div class='survey-tooltip'><span>?</span><p class='tooltip-text'>Data level 2: Confidential information - only users with a purely work-related need may and can have access to, and where a breach of confidentiality will have semi-serious impacts for the parties involved. Data level 3: sensitive information - due to its personal, technical, commercial, or competitive nature and sensitivity, must be protected against unintentional access and disclosure.</p></div></span>"],
                        next: [
                            {
                                hpc: ["AI-LAB", "UCloud", "Strato"],
                                question: "What type of processing power is required for your work?",
                                options: [
                                    "GPU-focused<span><div class='survey-tooltip'><span>?</span><p class='tooltip-text'>My work involves tasks like machine learning, deep learning, or other GPU-accelerated computations that benefit from parallel processing capabilities.</p></div></span>",
                                    "CPU-focused<span><div class='survey-tooltip'><span>?</span><p class='tooltip-text'>My work involves general computations, high-performance simulations, or tasks that rely on the strong sequential processing power of CPUs.</p></div></span>",
                                    "It requires efficiency of both CPU and GPU equally<span><div class='survey-tooltip'><span>?</span><p class='tooltip-text'>My work requires a combination of GPU and CPU resources to handle a diverse set of computational tasks efficiently.</p></div></span>",
                                    "I don't know"
                                ],
                                next: [
                                    {
                                        hpc: ["AI-LAB", "UCloud"],
                                        question: "Which capability is most crucial for your work?",
                                        options: [
                                            "My work requires training and deploying machine learning models, image recognition models, or large language models.",
                                            "I need a platform that supports a wide range of scientific applications, visualization tools etc."
                                        ],
                                        next: ["AI-LAB", "UCloud"]
                                    },
                                    {
                                        hpc: ["UCloud", "Strato"],
                                        question: "What type of interface do you prefer for interacting with the HPC platform?",
                                        options: [
                                            "I prefer a user-friendly environment with visual tools for easier navigation and management of my tasks.",
                                            "I am comfortable using terminal commands for precise control and efficient execution of my tasks."
                                        ],
                                        next: ["UCloud", "Strato"]
                                    },
                                    {
                                        hpc: ["UCloud", "Strato"],
                                        question: "What type of interface do you prefer for interacting with the HPC platform?",
                                        options: [
                                            "I prefer a user-friendly environment with visual tools for easier navigation and management of my tasks.",
                                            "I am comfortable using terminal commands for precise control and efficient execution of my tasks."
                                        ],
                                        next: ["UCloud", "Strato"]
                                    },
                                    {
                                        hpc: ["AI-LAB", "UCloud"],
                                        question: "Which capability is most crucial for your work?",
                                        options: [
                                            "My work requires training and deploying machine learning models, image recognition models, or large language models.",
                                            "I need a platform that supports a wide range of scientific applications, visualization tools etc."
                                        ],
                                        next: ["AI-LAB", "UCloud"]
                                    }
                                ]
                            },
                            "UCloud"
                        ]
                    },
                    {
                        hpc: ["AI Cloud", "UCloud", "Strato"],
                        question: "Do you need to process or store confidential or sensitive data?",
                        options: ["I'm only working on data levels 0, 1<span><div class='survey-tooltip'><span>?</span><p class='tooltip-text'>Data level 0: Public information. Data level 1: Internal information - only users with a purely work-related need may and can have access to.</p></div></span>", "I will include data levels 2, 3<span><div class='survey-tooltip'><span>?</span><p class='tooltip-text'>Data level 2: Confidential information - only users with a purely work-related need may and can have access to, and where a breach of confidentiality will have semi-serious impacts for the parties involved. Data level 3: sensitive information - due to its personal, technical, commercial, or competitive nature and sensitivity, must be protected against unintentional access and disclosure.</p></div></span>"],
                        next: [
                            {
                                hpc: ["AI Cloud", "UCloud", "Strato"],
                                question: "What type of processing power is required for your work?",
                                options: [
                                    "GPU-focused<span><div class='survey-tooltip'><span>?</span><p class='tooltip-text'>My work involves tasks like machine learning, deep learning, or other GPU-accelerated computations that benefit from parallel processing capabilities.</p></div></span>",
                                    "CPU-focused<span><div class='survey-tooltip'><span>?</span><p class='tooltip-text'>My work involves general computations, high-performance simulations, or tasks that rely on the strong sequential processing power of CPUs.</p></div></span>",
                                    "It requires efficiency of both CPU and GPU equally<span><div class='survey-tooltip'><span>?</span><p class='tooltip-text'>My work requires a combination of GPU and CPU resources to handle a diverse set of computational tasks efficiently.</p></div></span>",
                                    "I don't know"
                                ],
                                next: [
                                    {
                                        hpc: ["AI Cloud", "UCloud"],
                                        question: "Which capability is most crucial for your work?",
                                        options: [
                                            "My work requires training and deploying machine learning models, image recognition models, or large language models.",
                                            "I need a platform that supports a wide range of scientific applications, visualization tools etc."
                                        ],
                                        next: ["AI Cloud", "UCloud"]
                                    },
                                    {
                                        hpc: ["UCloud", "Strato"],
                                        question: "What type of interface do you prefer for interacting with the HPC platform?",
                                        options: [
                                            "I prefer a user-friendly environment with visual tools for easier navigation and management of my tasks.",
                                            "I am comfortable using terminal commands for precise control and efficient execution of my tasks."
                                        ],
                                        next: ["UCloud", "Strato"]
                                    },

                                    {
                                        hpc: ["UCloud", "Strato"],
                                        question: "What type of interface do you prefer for interacting with the HPC platform?",
                                        options: [
                                            "I prefer a user-friendly environment with visual tools for easier navigation and management of my tasks.",
                                            "I am comfortable using terminal commands for precise control and efficient execution of my tasks."
                                        ],
                                        next: ["UCloud", "Strato"]
                                    },
                                    {
                                        hpc: ["AI Cloud", "UCloud"],
                                        question: "Which capability is most crucial for your work?",
                                        options: [
                                            "My work requires training and deploying machine learning models, image recognition models, or large language models.",
                                            "I need a platform that supports a wide range of scientific applications, visualization tools etc."
                                        ],
                                        next: ["AI Cloud", "UCloud"]
                                    }
                                ]
                            },
                            "UCloud"
                        ]
                    },
                    {
                        hpc: ["AI-LAB", "UCloud"],
                        question: "What type of compilation resources do your students need for their coursework and research projects?",
                        options: [
                            "My students are engaged in projects involving training and deploying ML models using TensorFlow and PyTorch.",
                            "My students use a versatile platform for scientific applications and visualization, prioritizing ease of use and collaboration."
                        ],
                        next: ["AI-LAB", "UCloud"]
                    }
                ]
            }
        ];

        const platforms = {
            ucloud: {
                title: [
                    {text: "UCloud"}
                ],
                description: [
                    {text: "UCloud is a HPC research platform from the SDU eScience Center, engineered to provide high-performance computing with a focus on ease of use. Through the Danish e-Infrastructure Cooperation (DeiC), CLAAUDIA can provide access to UCloud."}
                ],
                hardware: [
                    {text: "Up to 192 VCPU", check: true},
                    {text: "Up to 768 GB memory", check: true},
                    {text: "Up to 8 GPUs per job", check: true}
                ],
                features: [
                    {text: "User-Friendly Interface", check: true},
                    {text: "Suitable for interactive jobs", check: true},
                    {text: "Can handle sensitive data", check: true},
                    {text: "Graphical User Interface", check: true}
                ],
                dataClassification: [
                    {text: "Data categories 0, 1, 2, 3", check: true}
                ],
                recommendedSkills: [
                    {text: "Minimal programming skills", check: true}
                ],
                link: [
                    {href: "https://www.researcher.aau.dk/guides/research-data/high-performance-computing/deic-hpc#interactive-hpc-(type-1)-(via-the-ucloud-platform)", text: "Learn more about UCloud"}
                ]
            },
            aicloud: {
                title: [
                    {text: "AI Cloud"}
                ],
                description: [
                    {text: "AI Cloud is a collection – a cluster – of large GPU servers and typically requires that users provide a container required to run their job. This makes the platform exceptionally flexible to your individual needs."}
                ],
                hardware: [
                    {text: "1000 GB storage", check: true},
                    {text: "Up to 48 GB memory per GPU", check: true},
                    {text: "Up to 8 GPUs per job", check: true},
                    {text: "Non vCPU centric system", check: false}
                ],
                features: [
                    {text: "Optimized for deep learning and AI tasks", check: true},
                    {text: "Container-based deployment", check: true},
                    {text: "Supports large-scale data processing", check: true},
                    {text: "Flexible resource allocation", check: true}
                ],
                dataClassification: [
                    {text: "Data categories 0, 1", check: true}
                ],
                recommendedSkills: [
                    {text: "Intermediate programming and containerization skills", check: true}
                ],
                link: [
                    {href: "https://www.researcher.aau.dk/guides/research-data/high-performance-computing/ai-cloud", text: "Learn more about AI Cloud"}
                ]
            },
            'ai-lab': {
                title: [
                    {text: "AI-LAB"}
                ],
                description: [
                    {text: "AI-LAB is a high-performance computing (HPC) platform developed for students and educators at Aalborg University. It functions like a mini supercomputer, equipped with advanced hardware, including NVIDIA GPUs, designed to handle computationally intensive tasks. Whether you're training deep learning models, analyzing large datasets, processing images and videos, or running complex simulations, AI-LAB provides the necessary power and flexibility."}
                ],
                hardware: [
                    {text: "1000 GB storage", check: true},
                    {text: "88 NVIDIA L4 GPUs", check: true},
                    {text: "62 GB memory per GPU", check: true},
                    {text: "Non vCPU centric system", check: false}
                ],
                features: [
                    {text: "Optimized for deep learning and AI tasks", check: true},
                    {text: "Container-based deployment", check: true},
                    {text: "Supports large-scale data processing", check: true},
                ],
                dataClassification: [
                    {text: "Data categories 0, 1", check: true}
                ],
                recommendedSkills: [
                    {text: "Intermediate programming and containerization skills", check: true}
                ],
                link: [
                    {href: "https://www.researcher.aau.dk/guides/research-data/high-performance-computing/ai-lab", text: "Learn more about AI-LAB"}
                ]
            },
            strato: {
                title: [
                    {text: "Strato"}
                ],
                description: [
                    {text: "The Strato platform is a cluster of hardware that is virtualised to create instances that essentially function as a regular computer environment. Strato Instances are virtual machines, that can be launched by the user when they need it. When the instance has been created, it can be accessed from a terminal application on the user's local computer."}
                ],
                hardware: [
                    {text: "Up to 128 vCPU", check: true},
                    {text: "Up to 250 GB vCPU memory", check: true},
                    {text: "Up to 3 GPUs per job", check: true},
                    {text: "Up to 64 GB memory per GPU", check: true},
                ],
                features: [
                    {text: "No maximum time of use", check: true},
                    {text: "All resources to yourself", check: true},
                    {text: "Possible to add GUI", check: true},
                    {text: "Store and process large datasets", check: true},
                ],
                dataClassification: [
                    {text: "Data categories 0, 1", check: true}
                ],
                recommendedSkills: [
                    {text: "Intermediate Linux and programming skills", check: true}
                ],
                link: [
                    {href: "https://www.researcher.aau.dk/guides/research-data/high-performance-computing/strato", text: "Learn more about Strato"}
                ]
            }
        };
        
        let currentPath = [];
        let currentQuestionIndex = 0;

        const questionTitle = document.getElementById('quiz-title');
        const questionContent = document.querySelector('.question-content');
        const remainingProgressBar = document.getElementById('remaining-progress-bar');
        const nextButton = document.querySelector('.next-btn');
        const previousButton = document.querySelector('.next-previous');
        const buttonContent = document.querySelector('.button-content');
        const quizBody = document.querySelector('.quiz-body');
        const finishedContent = document.querySelector('.finished');
        const resetButton = document.getElementById('reset-btn');
        const quizTitleHint = document.getElementById('quiz-title-hint');

        function calculateLongestPath(question) {
            if (typeof question === 'string') return 0;
            if (!question.next) return 1;

            return 1 + Math.max(...question.next.map(calculateLongestPath));
        }

        const totalQuestions = calculateLongestPath(quizData[0]);

        function renderQuestion() {
            const questionData = getCurrentQuestion();
            questionTitle.textContent = questionData.question;
            questionContent.innerHTML = '';

            if (questionTitle.textContent == "Do you need to process or store confidential or sensitive data?") {
                quizTitleHint.innerHTML = `
                <span>Not sure what type your data is? </span><a target="_blank" href="https://www.security.aau.dk/data-classification">Click here</a><span> to learn moreabout how to classify your information according to the AAU data classification model.</span>`;
            } else {
                quizTitleHint.innerHTML = ``;
            }

            questionData.options.forEach((option, i) => {
                const formCheck = document.createElement('div');
                formCheck.className = 'form-check question-option';
                formCheck.innerHTML = `
                    <input class="form-check-input" type="radio" name="quizOptions" id="option${i}">
                    <label class="form-check-label question-option-content" for="option${i}">
                        ${option}
                    </label>
                `;
                questionContent.appendChild(formCheck);
            });

            const remainingQuestions = totalQuestions - currentPath.length;
            const progressPercentage = ((totalQuestions - remainingQuestions) / totalQuestions) * 100;
            remainingProgressBar.style.width = `${progressPercentage}%`;
            remainingProgressBar.textContent = `${Math.round(progressPercentage)}%`;

            nextButton.style.display = 'none';
            previousButton.style.display = currentPath.length === 0 ? 'none' : 'inline-block';

            document.querySelectorAll('input[name="quizOptions"]').forEach(option => {
                option.addEventListener('change', () => {
                    document.querySelectorAll('.form-check').forEach(element => {
                        element.classList.remove('selected');
                    });
                
                    // Add the 'selected' class to the parent .form-check element of the checked input
                    if (option.checked) {
                        option.closest('.form-check').classList.add('selected');
                    }
                
                    nextButton.style.display = 'inline-block';
                });
            });

            updateButtonLayout();
        }

        function updateButtonLayout() {
            if (currentPath.length === 0) {
                buttonContent.style.justifyContent = 'right';
            } else {
                buttonContent.style.justifyContent = 'space-between';
            }
        }


        function getCurrentQuestion() {

            let question = quizData[currentQuestionIndex];
            currentPath.forEach(index => {
                question = question.next[index];
            });
            return question;
        }

        function getNextQuestionIndex(selectedOption) {
            let question = quizData[currentQuestionIndex];
            currentPath.forEach(index => {
                question = question.next[index];
            });
            if (question.next && question.next[selectedOption]) {
                return question.next[selectedOption];
            }
            return null;
        }

        function displayResult(result) {
            console.log("Result:", result); // Add this line for debugging
        
            quizBody.style.display = 'none';
            finishedContent.style.display = 'block';
        
            // Check if the platform exists
            const platformKey = result.toLowerCase().replace(/ /g, '');
            const platform = platforms[platformKey];
        
            if (!platform) {
                console.error("Platform not found for key:", platformKey);
                return;
            }
        
            // Populate title
            document.getElementById('spec-title').textContent = platform.title[0].text;
        
            // Populate description
            document.getElementById('spec-description').textContent = platform.description[0].text;
        
            // Clear and populate sections
            resetSection('HARDWARE SPECIFICATIONS');
            populateSection('HARDWARE SPECIFICATIONS', platform.hardware);
        
            resetSection('KEY FEATURES');
            populateSection('KEY FEATURES', platform.features);
        
            resetSection('DATA CLASSIFICATION');
            populateSection('DATA CLASSIFICATION', platform.dataClassification);
        
            resetSection('RECOMMENDED SKILLS');
            populateSection('RECOMMENDED SKILLS', platform.recommendedSkills);
        
            // Set link
            const linkElement = document.querySelector('.go-to-hpc-btn');
            linkElement.href = platform.link[0].href;
            linkElement.textContent = platform.link[0].text;
        
            // Reset progress bar
            remainingProgressBar.style.width = '100%';
            remainingProgressBar.textContent = '100%';
        
            nextButton.style.display = 'none';
            previousButton.style.display = 'none';
        }
        
        

        function populateSection(sectionTitle, items) {
            const section = Array.from(document.querySelectorAll('.option-item')).find(item => {
                return item.querySelector('.option-item-title').textContent === sectionTitle;
            });

            if (section) {
                items.forEach(item => {
                    const div = document.createElement('div');
                    div.className = 'option-item-item';
                    div.innerHTML = `
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="${item.check ? '#198754' : '#dc3545'}" class="bi bi-${item.check ? 'check' : 'x'}-square-fill" viewBox="0 0 16 16">
                            <path d="${item.check ? 
                            'M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2zm10.03 4.97a.75.75 0 0 1 .011 1.05l-3.992 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.75.75 0 0 1 1.08-.022z' : 
                            'M14 2a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12zM4.646 4.646a.5.5 0 0 0-.708.708L7.293 8l-3.355 3.354a.5.5 0 1 0 .708.708L8 8.707l3.646 3.647a.5.5 0 0 0 .708-.708L8.707 8l3.647-3.646a.5.5 0 0 0-.708-.708L8 7.293 4.646 4.646z'}"/>
                        </svg>                                    
                        <p class="option-item-item-body">${item.text}</p>
                    `;
                    section.appendChild(div);
                });
            }
        }
        function resetSection(sectionTitle) {
            // Find the section that matches the given title
            const sections = document.querySelectorAll('.option-item');
            sections.forEach(section => {
                const titleElement = section.querySelector('.option-item-title');
                if (titleElement && titleElement.textContent === sectionTitle) {
                    // Find all items within this section and remove them
                    const itemsToRemove = section.querySelectorAll('.option-item-item');
                    itemsToRemove.forEach(item => item.remove());
                }
            });
        }
        nextButton.addEventListener('click', () => {
            const selectedOption = document.querySelector('input[name="quizOptions"]:checked');
            if (selectedOption) {
                const selectedOptionIndex = Array.from(document.querySelectorAll('input[name="quizOptions"]')).indexOf(selectedOption);
                const nextQuestion = getNextQuestionIndex(selectedOptionIndex);
                if (typeof nextQuestion === 'string') {
                    displayResult(nextQuestion);
                } else {
                    currentPath.push(selectedOptionIndex);
                    renderQuestion();
                }
            }
        });

        previousButton.addEventListener('click', () => {
            if (currentPath.length > 0) {
                currentPath.pop();
                renderQuestion();
            }
        });
        
        resetButton.addEventListener('click', () => {
            currentPath = [];
            currentQuestionIndex = 0;
            quizBody.style.display = 'block';
            finishedContent.style.display = 'none';
            renderQuestion(); // Reset the quiz to the initial state
        });
            

        renderQuestion();
    }

    document.addEventListener('DOMContentLoaded', initializePage, false);


    document$.subscribe(() => {
        initializePage();
    });        

</script>

