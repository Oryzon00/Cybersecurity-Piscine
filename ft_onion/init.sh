#Tor service
/etc/init.d/tor restart

#ssh service
/usr/sbin/sshd;

#Path to tor hostname
echo "tor hostname:"
cat /var/lib/tor/my_website/hostname

#nginx service
nginx -g "daemon off;"
