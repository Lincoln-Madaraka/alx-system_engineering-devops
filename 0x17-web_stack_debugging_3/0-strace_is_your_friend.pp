#server error

exec { 'fix 500 error':
    path    => '/var/www/html/wp-settings.php',
    command => '/bin/sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
