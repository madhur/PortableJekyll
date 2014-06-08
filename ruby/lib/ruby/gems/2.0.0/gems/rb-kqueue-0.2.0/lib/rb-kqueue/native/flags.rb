module KQueue
  module Native
    # A module containing all the C-level integer flags
    # that are used with kqueue.
    #
    # @private
    module Flags
      # Filters
      EVFILT_READ = -1
      EVFILT_WRITE = -2
      EVFILT_AIO = -3 # Attached to aio requests
      EVFILT_VNODE = -4 # Attached to vnodes
      EVFILT_PROC = -5 # Attached to struct proc
      EVFILT_SIGNAL = -6 # Attached to struct proc
      EVFILT_TIMER = -7 # Timers
      EVFILT_MACHPORT = -8 # Mach portsets
      EVFILT_FS = -9 # Filesystem events
      EVFILT_USER = -10 # User events
      EVFILT_SESSION = -11 # Audit session events


      # Actions
      EV_ADD = 0x0001 # Add event to kq (implies enable)
      EV_DELETE = 0x0002 # Delete event from kq
      EV_ENABLE = 0x0004 # Enable event
      EV_DISABLE = 0x0008 # Disable event (not reported)
      EV_RECEIPT = 0x0040 # Force EV_ERROR on success, data == 0

      # Flags
      EV_ONESHOT = 0x0010 # Only report one occurrence
      EV_CLEAR = 0x0020 # Clear event state after reporting
      EV_DISPATCH = 0x0080 # Disable event after reporting

      # Returned values
      EV_EOF = 0x8000 # EOF detected
      EV_ERROR = 0x4000 # Error, data contains errno


      # For `EVFILT_{READ,WRITE}`
      NOTE_READ_LOWAT = NOTE_WRITE_LOWAT = 0x00000001 # Low water mark

      # For `EVFILT_VNODE`
      NOTE_VNODE_DELETE = 0x00000001 # Vnode was removed
      NOTE_VNODE_WRITE = 0x00000002 # Data contents changed
      NOTE_VNODE_EXTEND = 0x00000004 # Size increased
      NOTE_VNODE_ATTRIB = 0x00000008 # Attributes changed
      NOTE_VNODE_LINK = 0x00000010 # Link count changed
      NOTE_VNODE_RENAME = 0x00000020 # Vnode was renamed
      NOTE_VNODE_REVOKE = 0x00000040 # Vnode access was revoked

      # For `EVFILT_PROC`
      NOTE_PROC_EXIT = 0x80000000 # Process exited
      NOTE_PROC_FORK = 0x40000000 # Process forked
      NOTE_PROC_EXEC = 0x20000000 # Process exec'd
      NOTE_PROC_REAP = 0x10000000 # Process reaped
      NOTE_PROC_SIGNAL = 0x08000000 # Received signal
      NOTE_PROC_TRACK = 0x00000001 # follow across forks
      NOTE_PROC_TRACKERR = 0x00000002 # could not track child
      NOTE_PROC_CHILD = 0x00000004 # am a child process

      # For `EVFILT_TIMER`
      NOTE_TIMER_SECONDS = 0x00000001 # data is seconds
      NOTE_TIMER_USECONDS = 0x00000002 # data is microseconds
      NOTE_TIMER_NSECONDS = 0x00000004 # data is nanoseconds
      NOTE_TIMER_ABSOLUTE = 0x00000008 # absolute timeout


      # Converts a list of flags to the bitmask that the C API expects.
      #
      # @param prefix [String] The prefix for the C names of the flags
      # @param flags [Array<Symbol>]
      # @return [Fixnum]
      def self.to_mask(prefix, flags)
        flags.map {|flag| const_get("#{prefix}_#{flag.to_s.upcase}")}.
          inject(0) {|mask, flag| mask | flag}
      end

      # Converts a bitmask from the C API into a list of flags.
      #
      # @param prefix [String] The prefix for the C names of the flags
      # @param mask [Fixnum]
      # @return [Array<Symbol>]
      def self.from_mask(prefix, mask)
        re = /^#{Regexp.quote prefix}_/
        constants.select do |sym|
          c = sym.to_s
          next false unless c =~ re
          const_get(c) & mask != 0
        end.map {|c| c.to_s.sub("#{prefix}_", "").downcase.to_sym}
      end

      # Converts a flag to the integer that the C API expects.
      #
      # @param prefix [String] The prefix for the C names of the flags
      # @param flag [Symbol]
      # @return [Fixnum]
      def self.to_flag(prefix, flag)
        const_get("#{prefix}_#{flag.to_s.upcase}")
      end

      # Converts an integer from the C API into a flag.
      #
      # @param prefix [String] The prefix for the C names of the flags
      # @param flag [Fixnum]
      # @return [Symbol]
      def self.from_flag(prefix, flag)
        re = /^#{Regexp.quote prefix}_/
        constants.each do |sym|
          c = sym.to_s
          next unless c =~ re
          return c.to_s.sub("#{prefix}_", "").downcase.to_sym if const_get(c) == flag
        end
      end
    end
  end
end
