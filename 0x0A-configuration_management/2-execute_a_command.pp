# creates a manifest that kills the process 'killmenow'

exec { 'pkill':
  command  => 'pkill -f killmenow',
  provider => 'shell',
}