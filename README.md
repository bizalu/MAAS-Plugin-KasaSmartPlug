Home
=========
Deploy your own private cloud.</br></br>

Configure your own Openstack with MaaS and JuJu
----------------
<p align="left">
  <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,c_fill,w_100,h_100/https://assets.ubuntu.com/v1/a7916513-picto-openstack.svg" title="Openstack">
  <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_100,h_100/https://assets.ubuntu.com/v1/0de4fcd5-logo-maas-icon.svg" title="MaaS">
  <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_100,h_100/https://assets.ubuntu.com/v1/60bd6cf1-picto-juju.svg" title="Juju">
</p>

We want to deploy openstack on 3 physicals node define in MaaS with tag "openstack".

<b>Base</b> : we use the charm bundle <a href="https://jaas.ai/openstack-base" target="_blank" title="Openstack Base">Openstack Base</a></br>
<b>Additionnals</b> : we use the extra charm <a href="https://jaas.ai/cinder-backup" target="_blank" title="Cinder Backup">Cinder Backup (backup)</a> and <a href="https://jaas.ai/designate" target="_blank" title="Designate">Designate (DNS)</a></br></br>

Configure your own K8S with JuJu on openstack
----------------
<p align="left">
  <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,c_fill,w_100,h_100/https://api.charmhub.io/api/v1/media/download/charm_935X4QPzHo77UEMt4pFVEppOBLdhm43M_icon__075ac8b5bd314f704c7f950d81bb5c1459578925797e6e8a445516804a4f381a.png" title="K8s">
  <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_100,h_100/https://assets.ubuntu.com/v1/60bd6cf1-picto-juju.svg" title="Juju">
</p>

<b>Base</b> : we use the charm bundle <a href="https://jaas.ai/kubernetes-core/bundle" target="_blank" title="kubernetes-core">Kubernetes core</a></br>
