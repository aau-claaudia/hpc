---
icon: lucide/cog
---


Key characteristics:

- Secure-by-design platform architecture 
- Support for sensitive and regulated research data 
- Flexible compute resources for data processing, AI, ML, and HPC workloads 
- Role-based access to data

---

## Platform Architecture

TAAURUS is structured in **four main layers**: 

1. **Frontend**  
   Project-specific virtual machines with preinstalled software packages. 

2. **Backend**  
   GPU servers for AI/ML and high-performance computing, managed through a [**Slurm**](https://slurm.schedmd.com/quickstart.html) queueing system. 

3. **Storage Platform**  
   Secure, high-performance storage with a separate protected storage area for each project. 

4. **Data Transfer Layer**  
   Controlled import and export services for moving data into and out of the platform. 

---

## Hardware and Compute Resources

!!! info "GPU compute cluster"
    The GPU compute environment is built for high-performance, GPU-accelerated workloads such as machine learning, AI training, and advanced data processing. 

### Compute node specification

Each of the **two physical compute nodes** includes: 

- **Model:** Lenovo SR675v3 
- **CPU:** Dual AMD EPYC 9354 (2 × 32 cores) 
- **Memory:** 768 GB RAM per node 
- **GPU:** 8 × NVIDIA L40S per node 
- **GPU memory:** 48 GB GDDR6 per GPU 
- **CUDA cores:** 18,176 per GPU 
- **Networking:** 2 × 100 Gbps Ethernet 

---

## Storage and Data Handling

### Secure storage

TAAURUS uses **Hitachi HCSF** as its high-performance storage platform.

Storage features include:

- project-specific secure storage areas 
- encryption at rest 
- high-performance flash storage 

### Data isolation

Each project is assigned its own dataset and storage area. Users cannot access datasets outside their own project scope. 

---

## Access and Authentication

User access requires:

- login through a **Remote Desktop Gateway** 
- **multi-factor authentication** 
- an **AAU account** 
- Connection to **AAU network**
- membership in the relevant project-specific AD groups 

---

## Security higlights

TAAURUS includes:

- isolation from the public internet
- role-based access control 
- project-based access separation 
- encrypted data transfer 
- encryption at rest on storage systems 
- controlled and logged import/export workflows 
- restricted network traffic via firewall rules 

---

## Data Import and Export

Import and export are controlled workflows and require approval within the platform governance model. 

### Import

- Data import requests are handled through **ServiceNow**. 
- Import must be approved by the **Principal Investigator (PI)**. 
- Imported data must be correctly classified and labelled. 

### Export

- Data export must also be approved by the **PI**. 
- Smaller exports can be transferred to a dedicated export web server for download. 
- Export workflows are logged and controlled. 
- The longer-term design includes automated transfers through **NiFi**. 

---

## Available Software

!!! note "Research tools"
    The platform provides access to a range of commonly used research and analysis tools. 

Available software includes:

- **LibreOffice Calc** 
- **LibreOffice Writer** 
- **Atril Document Viewer** 
- **DICOMscope** and **Weasis** 
- **R** and **RStudio** 
- **Python** and **Anaconda** 
- **Stata** 
- **Matlab** 

Software packages can be updated by ITS through service requests. 
