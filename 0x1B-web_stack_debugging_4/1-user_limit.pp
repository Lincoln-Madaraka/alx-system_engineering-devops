# increase the soft and hard limit for holberton use
exec {'increase hard limit':
    path    => '/etc/security/limits.conf',
    command => "/bin/sed -i 's/holberton hard nofile 5/holberton hard nofile 8000/g' /etc/security/limits.conf"
}

exec {'increase soft limit':
    path    => '/etc/security/limits.conf',
    command => "/bin/sed -i 's/holberton soft nofile 4/holberton hard nofile 4000/g' /etc/security/limits.conf"
}
