How to install MAAS with Kasa SmartPlug integration
===================================================

Install MAAS (rack+controler)
---------------------
**Install the prerequis (only on ubuntu focal 20.04) :**
```bash
sudo apt-add-repository -yu ppa:maas/3.1
```

**Install postgresql and MAAS server :**
```bash
sudo apt install -y postgresql maas
```

**Configure the admin account for MAAS server :**
```bash
export MAAS_ADMUSER="admin" && export MAAS_ADMPASS=`openssl rand -base64 32` && sudo maas createadmin --username $MAAS_ADMUSER --password $MAAS_ADMPASS --email "admin@exemple.com" && echo "Your admin account is $MAAS_ADMUSER with the password $MAAS_ADMPASS, don't lose it"
```

I don't know why, but I need to execute this command to debug bind9 :
```bash
sudo chown bind:root /var/cache/bind/
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

Configure your server as an hotspot wifi (optional)
---------------------
You can associate your Kasa SmartPlug on a dedicated wifi network, with this command :
```bash
sudo apt install -y network-manager
```
```bash
export WIFI_SSID="power" && export WIFI_PASS=`openssl rand -base64 16` && sudo nmcli d wifi hotspot ifname wlp3s0 ssid $WIFI_SSID password $WIFI_PASS && echo "Your wifi hotspot is $WIFI_SSID with the password $WIFI_PASS, don't lose it"
```

To start the wifi hotspot on boot, edit the file :
```bash
sudo vi /etc/NetworkManager/system-connections/Hotspot.nmconnection
```

And change the paramater "autoconnect" to "true".
