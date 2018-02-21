SELinux policy module can be built from these files.

Required packages are the following (at least on a Centos system):

    setools-console
    policycoreutils-python-2.5-17.1.el7    // This package provides binary file /usr/sbin/semanage
    policycoreutils-devel                  // Requiered development files needed to code SELinux modules.

Bear in mind, in order to use this SELinux module to confine webapp create the python virtualenv
under the user home directory e.g: /home/rtxapps/.venvs/flask-web-fortune

Reminder for venv:

virtualenv /home/rtxapps/.venvs/flask-web-fortune
source /home/rtxapps/.venvs/flask-web-fortune/bin/activate
pip install -r /path/to/requirements.txt







