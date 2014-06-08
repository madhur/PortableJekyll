module KQueue
  class Watcher
    # The {Watcher} subclass for events fired when a file changes.
    # File events are watched via {Queue#watch_file}.
    class File < Watcher
      # The path to the file being watched.
      #
      # @return [String]
      attr_reader :path

      # Creates a new file Watcher.
      #
      # @private
      def initialize(queue, path, flags, callback)
        @path = path
        @fd = Native.open(path, 0) # 0 means "read only"

        if @fd < 0
          raise SystemCallError.new(
            "Failed to open file #{path}" +
            case FFI.errno
            when Errno::EACCES::Errno; ": Permission denied."
            when Errno::EAGAIN::Errno; ": Slave side of a locked pseudo-terminal device."
            when Errno::EFAULT::Errno; ": Outside the process's allocated address space."
            when Errno::EINTR::Errno; ": Interrupted."
            when Errno::ELOOP::Errno; ": Too many symbolic links (possible loop)."
            when Errno::EMFILE::Errno; ": Too many open files."
            when Errno::ENAMETOOLONG::Errno; ": Name too long."
            when Errno::ENFILE::Errno; ": System file table is full."
            when Errno::ENOENT::Errno; ": File doesn't exist."
            when Errno::ENOTDIR::Errno; ": A component of the path prefix is not a directory."
            when Errno::ENXIO::Errno; ": The device associated with this file doesn't exist."
            when Errno::EOPNOTSUPP::Errno; ": File type not supported."
            when Errno::EOVERFLOW::Errno; ": File too big."
            else; ""
            end,
            FFI.errno)
        end

        ObjectSpace.define_finalizer(self, lambda do
            next unless Native.close(@fd) < 0
            raise SystemCallError.new(
              "Failed to close file #{path}" +
              case FFI.errno
              when Errno::EBADF::Errno; ": Invalid file descriptor."
              when Errno::EINTR::Errno; ": Closing interrupted."
              when Errno::EIO::Errno; ": IO error."
              else; ""
              end,
              FFI.errno)
          end)
        super(queue, @fd, :vnode, flags, nil, callback)
      end
    end
  end
end
