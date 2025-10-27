# Navigating TAAURUS

This guide will help you navigate the platform, understand the available applications, and work with the file system effectively.

## Desktop Overview

When you first log into TAAURUS, you'll see a Windows desktop environment with several key components:

- **Desktop Icons**: Shortcuts to commonly used applications
- **Taskbar**: Quick access to running applications and system functions
- **Start Menu**: Access to all installed software and system tools
- **File Explorer**: Navigate and manage your files and folders

![Screenshot of TAAURUS](/assets/img/taaurus/taaurus-server-2.png)

## Available Applications

TAAURUS comes pre-installed with applications for research and high-performance computing:

### Scientific and Statistical Software

- R and RStudio
- Python and Anaconda
- MATLAB
- Stata

### Medical and Imaging Software
- DICOMscope: Medical imaging viewer for DICOM files
- Weasis: Advanced medical image viewer

### Office Applications

- LibreOffice Calc: Spreadsheet application for data analysis
- LibreOffice Writer: Word processing for documentation and reports
- PDF Reader: Atril Document Viewer for viewing research documents
- Pluma: Simple text editor

### Terminal
- MATE Terminal

## File System Navigation

### Project-Specific Storage

TAAURUS provides dedicated, secure storage for each project located in `/media/yourproject`:

```
/media/yourproject/
├── data/          # Your project's dataset
├── work/          # Scripts and other project relevant files
└── export/        # Files and folders ready for exporting
```

### File Management Best Practices

- **Project Organization**: Keep all project files in your dedicated storage area. Do not use your own storage (`/home/domain/user`)

## Working with Applications

### Starting Applications

#### From Start Menu
1. Click the **Start** button
2. Browse or search for your application
3. Click to launch

#### From Desktop
1. Double-click application shortcuts
2. Right-click for additional options

#### From Command Line
- Open Windows Terminal or Command Prompt
- Type the application name (e.g., `code`, `jupyter notebook`)

### Application Management

#### **Switching Between Applications**
- Use **Alt + Tab** to cycle through open applications
- Click on taskbar icons to switch to specific applications
- Use **Windows + Tab** for a visual overview

#### **Closing Applications**
- Click the **X** button in the top-right corner
- Use **Alt + F4** to close the active application
- Right-click taskbar icons for close options

## Network and Storage

### TAAURUS Storage Architecture

#### **High-Performance Storage**
- **Hitachi HCSF**: High-performance distributed file system
- **8-node cluster**: High-performance flash-tier storage
- **Encrypted Storage**: All data encrypted at rest
- **Project Isolation**: Each project has dedicated, secure storage areas

#### **Storage Features**
- **High Performance**: Optimized for HPC, AI, ML, and analytical workloads
- **Scalability**: Can scale to meet project requirements
- **Disaster Recovery**: Automated backup with Hitachi HCP
- **Security**: Built-in security features and access control

### Network Security

#### **Isolated Network**
- **Internal Network**: Isolated from the internet for security
- **Firewall Protection**: Technical measures prevent unauthorized data transmission
- **Controlled Access**: Limited network access for necessary functions only
- **Secure Gateways**: Dedicated RDP and SSH gateways for secure access

#### **Data Security**
- **No Internet Access**: Data cannot accidentally leave the platform
- **Encrypted Transfers**: All data transfers use encrypted connections
- **Access Logging**: Complete audit trail of all network activity
- **Compliance**: Meets GDPR and ISO 27001/27701 requirements

## Getting Help

### Built-in Help
- **F1 Key**: Context-sensitive help in most applications
- **Help Menus**: Available in most applications
- **Documentation**: Check application-specific documentation

### Support Resources
- **CLAAUDIA Support**: [serviceportal.aau.dk](https://serviceportal.aau.dk/serviceportal?id=sc_cat_item&sys_id=a05e2fb4c3434610f0f3041ad00131d0)
- **User Forums**: Connect with other TAAURUS users
- **Documentation**: Platform-specific guides and tutorials

## Tips for Success

### Security Best Practices
1. **Data Classification**: Always properly classify and label your data
2. **Secure Handling**: Follow security procedures for sensitive data
3. **Access Control**: Only access data you're authorized to use
4. **Documentation**: Maintain proper documentation of your work

### Performance Optimization
1. **Close Unused Applications**: Free up system resources
2. **Organize Files**: Keep your project workspace tidy
3. **Regular Cleanup**: Remove temporary files to maintain performance
4. **Monitor Resources**: Use Task Manager to check system usage

### Collaboration
1. **Project Team**: Work with authorized project members only
2. **Version Control**: Use Git for code collaboration
3. **Documentation**: Document your work for team members
4. **Compliance**: Follow all security and compliance procedures

## Next Steps

Now that you understand the TAAURUS interface, you're ready to:

1. **Start Your Project**: Begin working with your project's secure dataset
2. **Explore Applications**: Try out the pre-installed software for your research
3. **Set Up Your Environment**: Configure your preferred development tools
4. **Begin Computing**: Start your high-performance computing tasks
5. **Follow Security Procedures**: Ensure compliance with all security requirements

For specific application guides and advanced topics, check out the additional TAAURUS documentation sections.