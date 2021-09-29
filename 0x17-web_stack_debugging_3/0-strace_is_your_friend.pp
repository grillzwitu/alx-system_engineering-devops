# fixes Apache 500 error by fixing typo in wordpress
exec { 'fix typo':
  onlyif  => 'test -e /var/www/html/wp-settings.php',
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin',
}
