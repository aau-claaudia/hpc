# Transferring files

Use **scp** (secure copy) to upload and download files between your local computer and AI-LAB.

---

## 📤 Uploading Files

```bash
scp -r myfile.txt user@student.aau.dk@ailab-fe01.srv.aau.dk:~
```

## 📥 Downloading Files

```bash
scp -r user@student.aau.dk@ailab-fe01.srv.aau.dk:~/myfile.txt .
```

* `-r` copies directories recursively
* `~` means your home directory on AI-LAB

---

## 💻 File managers (recommended)
For Windows users, we recommend [**WinSCP**](https://winscp.net/eng/download.php). 

For Linux, macOS, or Windows (cross-platform), we recommend [**Double Commander**](https://sourceforge.net/p/doublecmd/wiki/Download/).

---

**Next:** [Slurm →](9-slurm.md)
