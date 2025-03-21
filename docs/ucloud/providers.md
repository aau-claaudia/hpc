# Providers on UCloud

UCloud supports several providers that cater to different research and computational needs. This guide covers three primary providers: SDU/K8s, AAU/K8s, and AAU/VM.

## SDU/K8s & AAU/K8s

Both SDU/K8s and AAU/K8s are Kubernetes-based environments designed for scalable research workloads. They allow users to quickly launch pre-built applications. However, there are important differences to consider before choosing one.

### SDU/K8s vs. AAU/K8s

- **SDU/K8s** provides:
  - ✅ Handling of **sensitive data**  
  - ✅ **SSH connections**  
  - ✅ Support for **licensed software**  
  - ✅ **Fixed IP addresses**

- **AAU/K8s**:
  - ❌ Does not accommodate **sensitive data**  
  - ❌ No **SSH access**  
  - ❌ No support for **licensed software**  
  - ❌ No **fixed IP addresses**  
  - ✅ Offers access to a **wide range of GPUs**

If you need any of the capabilities listed for SDU/K8s—such as handling sensitive data, requiring SSH connections, or leveraging licensed software — choose SDU/K8s. 

---

## AAU/VM

**AAU/VM** is a traditional virtual machine provider for users requiring full control over their environment.

### Key Features:

- ✅ Customizable **virtual machines**  
- ✅ **GPU support** for compute-heavy tasks  
- ✅ Complete **OS control** for specialized or custom software installations

AAU/VM is ideal if you need an environment where you can configure the operating system extensively or run GPU-intensive workloads that demand tight control over system settings.
