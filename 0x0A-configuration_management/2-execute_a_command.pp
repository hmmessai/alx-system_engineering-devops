# Kills a process named killmenow
exec { 'pkill':
  command => 'pkill -15 -f killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
