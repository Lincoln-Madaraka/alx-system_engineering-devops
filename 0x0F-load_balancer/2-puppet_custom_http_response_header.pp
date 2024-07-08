#  install and configure an Nginx server
exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package { 'nginx':
  ensure => installed,
}
-> file_line { 'header_served_by':
  path     => '/etc/nginx/sites-available/default',
  after    => 'server_name _;',
  line     => "\n\tadd_header X-Served-By \"${hostname}\";",
  multiple => false,
}
-> exec {'restart':
  command => '/usr/sbin/service nginx restart',
} 
