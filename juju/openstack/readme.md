Install openstack bundle
==========

Install openstack with juju :
---------------
```bash
juju add-model openstack
```
```bash
juju deploy ./bundle.yaml
```

And you can view the installation status with the command :
```bash
juju status
```

Unsealed Vault:
-------------
```bash
sudo snap install vault
```
```bash
export VAULT_IP=`juju status | grep vault/ | awk '{ print $5":"$6}' | awk -F"/" '{ print $1}'`
export VAULT_ADDR="http://$VAULT_IP"
```
```bash
vault operator init -key-shares=5 -key-threshold=3
```
```vim
Unseal Key 1: ############################
Unseal Key 2: ############################
Unseal Key 3: ############################
Unseal Key 4: ############################
Unseal Key 5: ############################

Initial Root Token: ############################
```
And now, you have to unseald with 3 Unseale key :
```bash
vault operator unseal
```
Create a new root token
```bash
export VAULT_TOKEN=<initial root token>
```
```bash
vault token create -ttl=10m
```
```bash
juju run-action --wait vault/leader authorize-charm token=<new root token>
```
```bash
juju run-action --wait vault/leader generate-root-ca
```

Get horizon dashboard admin password:
----------------
```bash
juju run --unit keystone/0 leader-get admin_passwd
```
