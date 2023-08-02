#!/usr/bin/bash

# adjust username in -u accordingly
# secure the password inside ansible-vault
ansible -m ping -u admin --vault-password-file host_vars/sandbox_aci/ping_cred.yml --vault-id @prompt sandbox_aci
