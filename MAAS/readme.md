How to install MAAS
====================


Configure static IP and install prerequis
---------------------
**Disable the network cloud manangement :**
```bash
sudo vi /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg
```
And add the line 
```vim
network: {config: disabled}
```

**Configure your static network :**
```bash
sudo vi /etc/netplan/01-netcfg.yaml
```
And add the line 
```vim
network:
  version: 2
  renderer: networkd
  ethernets:
    ens192:
      dhcp4: no
      addresses:
        - <your IP/MASK>
      gateway4: <your gateway>
      nameservers:
        addresses: [<your DNS server>]
```
Apply the configuration
```bash
sudo netplan apply
```
**Install the prerequis :**
```bash
sudo apt-add-repository -yu ppa:maas/3.0
sudo apt update
sudo apt upgrade -y
```

Install MAAS (rack+controler)
---------------------
**Install postgresql server**
```bash
sudo apt install -y postgresql
```
**Install MAAS server**
```bash
sudo apt install -y maas
```
**Configure the admin account for MAAS server**
```bash
export MAAS_ADMUSER="admin"
export MAAS_ADMPASS=`openssl rand -base64 32`
sudo maas createadmin --username $MAAS_ADMUSER --password $MAAS_ADMPASS --email "admin@exemple.com"
echo "Your admin account is $MAAS_ADMUSER with the password $MAAS_ADMPASS, don't lose it"
```

Install the custom power plugin
---------------------
```bash
sudo apt install -y python3-pip
```
```bash
sudo pip3 install --system  python-kasa
```
```bash
sudo cp ./powerkasa.py /usr/lib/python3/dist-packages/provisioningserver/drivers/power/
sudo chown root:root /usr/lib/python3/dist-packages/provisioningserver/drivers/power/powerkasa.py
sudo chmod 644 /usr/lib/python3/dist-packages/provisioningserver/drivers/power/powerkasa.py
```
```
