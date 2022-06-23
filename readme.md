How to install MAAS with Kasa SmartPlug integration
===================================================

Install MAAS (rack+controler)
---------------------
**Install the prerequis (only on ubuntu focal 20.04) :**
```bash
sudo apt-add-repository -yu ppa:maas/3.2
sudo apt update && sudo apt upgrade -y
```

**Install postgresql server :**
```bash
sudo apt install -y postgresql
```

**Install MAAS server :**
```bash
sudo apt install -y maas
```

**Configure the admin account for MAAS server :**
```bash
export MAAS_ADMUSER="admin"
export MAAS_ADMPASS=`openssl rand -base64 32`
sudo maas createadmin --username $MAAS_ADMUSER --password $MAAS_ADMPASS --email "admin@exemple.com"
echo "Your admin account is $MAAS_ADMUSER with the password $MAAS_ADMPASS, don't lose it"
```

Install the custom power plugin
---------------------
**Install the prerequis :**
```bash
sudo apt install -y python3-pip
```
```bash
sudo pip3 install --system  python-kasa
```

**Install the custom driver and patch MAAS :**

The file "powerKasa.py" and "patch.registry" must be present in the current directory before begin.
```bash
sudo cp ./powerkasa.py /usr/lib/python3/dist-packages/provisioningserver/drivers/power/
sudo chown root:root /usr/lib/python3/dist-packages/provisioningserver/drivers/power/powerkasa.py
sudo chmod 644 /usr/lib/python3/dist-packages/provisioningserver/drivers/power/powerkasa.py
```
```bash
sudo patch /usr/lib/python3/dist-packages/provisioningserver/drivers/power/registry.py < patch.registry
```

**Reboot the MAAS server to apply :**
```bash
sudo shutdown -r now
```
