# increase the soft limit for nginx
exec {'increase soft limit':
    path    => '/etc/default/nginx',
    command => "/bin/sed -i 's/15/4096/g' /etc/default/nginx"
}

service {'nginx restart':
    ensure    => running,
    name      => 'nginx',
    enable    => true,
    subscribe => Exec['increase soft limit'],
}

