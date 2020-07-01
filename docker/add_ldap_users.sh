#!/bin/bash

ldapadd -x -D "cn=admin,dc=example,dc=org" -w admin -h localhost -p 389 -f hollywood.ldif
