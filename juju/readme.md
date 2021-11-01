Install Juju MAAS controler
====================

```bash
sudo snap install juju --classic
juju add-cloud --client
```

Select cloud type: ***maas***

Enter a name for your maas cloud: ***maas.elserverido.com***

Enter the API endpoint url: ***MAAS URL (http://IP:5240/MAAS/)***

```bash
juju add-credential maas.elserverido.com
```

Enter credential name: ***maas-credential***

Enter maas-oauth: ***MAAS API KEY***

```bash
juju bootstrap --constraints tags=juju maas.elserverido.com
```
