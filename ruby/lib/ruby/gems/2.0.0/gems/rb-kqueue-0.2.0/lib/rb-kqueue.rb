require 'rb-kqueue/native'
require 'rb-kqueue/native/flags'
require 'rb-kqueue/watcher'
require 'rb-kqueue/watcher/file'
require 'rb-kqueue/watcher/read_write'
require 'rb-kqueue/watcher/process'
require 'rb-kqueue/event'
require 'rb-kqueue/queue'

# The root module of the library, which is laid out as so:
#
# * {Queue} -- The main class, where events are registered
# * {Watcher} -- A watcher for a single sort of event
# * {Event} -- A notification that an event has occurred
module KQueue
  VERSION = [0, 2, 0]

  # Raise an exception for a native kqueue error.
  #
  # @param errno [Fixnum] The errno identifying the sort of error.
  #   This is usually C's `errno` variable,
  #   but is sometimes set in a kevent struct
  # @raise [SystemCallError]
  # @private
  def self.handle_error(errno = FFI.errno)
    raise SystemCallError.new(
      "KQueue failed" +
      case errno
      when Errno::EFAULT::Errno; ": There was an error reading or writing the kevent structure."
      when Errno::EBADF::Errno; ": The specified descriptor is invalid."
      when Errno::EINTR::Errno; ": A signal was delivered before the timeout expired and before any events were placed on the kqueue for return."
      when Errno::EINVAL::Errno; ": The specified time limit or filter is invalid."
      when Errno::ENOENT::Errno; ": The event could not be found to be modified or deleted."
      when Errno::ENOMEM::Errno; ": No memory was available to register the event."
      when Errno::ESRCH::Errno; ": The specified process to attach to does not exist."
      else; ""
      end,
      errno)
  end
end
