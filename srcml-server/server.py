#!/usr/bin/env python3

import socket
import subprocess

with socket.socket() as s:
    s.bind(('', 5678))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        with conn:
            print ('Connected by ', addr)
            print ('receiving file to process ..')
            with open('remote-file.c', 'wb') as f:
                data = conn.recv(1024)
                while (data):
                    f.write(data)
                    data = conn.recv(1024)
            print ('received. Running srcml ..')
            # call srcml on the file
            # proc = subprocess.run(['srcml', '--simple', '--position', 'remote-file.c'], stdout=subprocess.PIPE)
             
            # proc = subprocess.run(['srcml',
            #                        '-f empty',
            #                        '--no-namespace-decl',
            #                        '--no-xml-declaration',
            #                        '--position',
            #                        'remote-file.c'], stdout=subprocess.PIPE)
            output = subprocess.check_output(['srcml',
                                              '-f empty',
                                              # '--no-namespace-decl',
                                              # '--no-xml-declaration',
                                              '--position',
                                              'remote-file.c'])
            print ('SrcML finished. Sending result back..')
            # print ('srcml output: ', proc.stdout)
            # conn.sendall(proc.stdout)
            conn.sendall(output)
            # with open('remote-output.xml', 'w') as f:
            #     f.write(proc.stdout)
            # with open('remote-output.xml', 'rb') as f:
            #     conn.sendfile(f)
            print ('Sent')
