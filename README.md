# Malicious-Debian-Package-Maker
Simple script to inject bash script inside any debian package. It utilises preinst and postinst scripts as a medium to run user defined bash script. **This script depends on dpkg-deb** command line to achieve it's task, so make sure you have it on your system.

# Install
```bash
git clone https://github.com/Trushal2004/Malicious-Debian-Package-Maker.git
cd Malicious-Debian-Package-Maker/
chmod +x main.py
./main.py
```
