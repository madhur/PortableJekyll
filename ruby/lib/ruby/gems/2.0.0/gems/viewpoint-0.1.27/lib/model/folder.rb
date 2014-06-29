=begin
  This file is part of Viewpoint; the Ruby library for Microsoft Exchange Web Services.

  Copyright © 2011 Dan Wanek <dan.wanek@gmail.com>

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
=end

module Viewpoint
  module EWS
    # This class represents a FolderType object in the Exchange Data store.
    # This is the type of folder that mail messages will be found in.
    class Folder < GenericFolder

      # Find folders of type Folder (message folders)
      # @see GenericFolder.find_folders
      # @param [String,Symbol] root An folder id, either a DistinguishedFolderId (must me a Symbol)
      #   or a FolderId (String)
      # @param [String] traversal Shallow/Deep/SoftDeleted
      # @param [String] shape the shape to return IdOnly/Default/AllProperties
      # @param [optional, String] folder_type an optional folder type to limit the search to like 'IPF.Task'
      # @return [Array] Returns an Array of Folder or subclasses of Folder
      def self.find_folders(root = :msgfolderroot, traversal = 'Deep', shape = 'Default', folder_type = 'IPF.Note')
        super(root, traversal, shape, folder_type)
      end


      # Initialize with an item of FolderType.  This is typically the folder
      # used to house mail messages.
      def initialize(folder)
        super(folder)
        define_int_var :unread_count
      end

    end # Folder
  end # EWS
end # Viewpoint
