# create a custom HTTP header response

exec {'HTTP_Header':
  command  => 'apt-get -y update && apt-get -y install nginx && echo "Holberton School" > /var/www/html/index.nginx-debian.html && HTTP_H="server_name _;\n\tadd_header X-Served-By $HOSTNAME;" && sed -i "s/server_name _;/$HTTP_H/" /etc/nginx/sites-available/default && service nginx restart',
  provider => shell,
}