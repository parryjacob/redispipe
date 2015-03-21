# redispipe

This is a wrapper command line utility to wrap the stdout/stdin of a process in
a set of Redis pubsub queues. All configuration is done through a set of
environment variables.

`REDISPIPE_URL` - the `redis://` URI to use

`REDISPIPE_QUEUE` - the prefix for the Redis pub/sub queue to use, defaults to
a useless value involving the MD5 sum of the command - you should *really*
set this or this entire thing will be useless. Note: if you are running using
`supervisord`, the queue will default to being `redispipe_<process_name>` where
`<process_name>` is the name of the `supervisord` process.

`REDISPIPE_QUIET` - don't output anything (Redis prefix, termination, etc)
