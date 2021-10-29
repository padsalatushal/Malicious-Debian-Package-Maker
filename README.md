# Malicious-Debian-Package-Maker
Simple script to inject bash script inside any debian package. It utilises preinst and postinst scripts as a medium to run user defined bash script. **This script depends on dpkg-deb** command line to achieve it's task, so make sure you have it on your system.

# Install
```bash
git clone https://github.com/Trushal2004/Malicious-Debian-Package-Maker.git
cd Malicious-Debian-Package-Maker/
chmod +x main.py
./main.py
```


# Help
```
$./main.py --help
usage: python3 ./main.py -p debian_package -s bash_script

Inject bash script in debian package

optional arguments:
  -h, --help         show this help message and exit
  -v, --version      show the version of program
  -s bash script     Enter your bash script path
  -p debian package  Enter your debian package path

EXAMPLE - python3 ./main.py -p /tmp/file.deb -s /tmp/script.sh
```

# Demo
![image](https://user-images.githubusercontent.com/57517785/139453947-710e8948-9ffe-419a-b771-46e33205f0bd.png)


![image](https://user-images.githubusercontent.com/57517785/139454081-edebad5f-3446-4350-8595-b56a3be03f86.png)
