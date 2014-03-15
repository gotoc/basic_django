<VirtualHost *:80>
        ServerAdmin webmaster@mydomain.com
        ServerName mydomain.com
        ServerAlias www.mydomain.com
        WSGIScriptAlias / var/www/mydomain.com/index.wsgi

        Alias /static/ /var/www/mydomain.com/static/
        <Location "/static/">
            Options -Indexes
        </Location>
</VirtualHost>
