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
    # This class represents a SearchFolderType object in the Exchange Data store.
    class SearchFolder < GenericFolder

      # Find folders of type SearchFolder
      # @see GenericFolder.find_folders
      # @param [String,Symbol] root An folder id, either a DistinguishedFolderId (must me a Symbol)
      #   or a FolderId (String).  SearchFolders must be created under the :searchfolders distinguished
      #   id so we might as well only search from there.
      # @param [String] traversal Shallow/Deep/SoftDeleted
      # @param [String] shape the shape to return IdOnly/Default/AllProperties
      # @param [optional, String] folder_type an optional folder type to limit the search to like 'IPF.Task'
      # @return [Array] Returns an Array of Folder or subclasses of Folder
      def self.find_folders(root = :searchfolders, traversal = 'Deep', shape = 'Default', folder_type = nil)
        super(root, traversal, shape, folder_type)
      end


      def initialize(folder)
        super(folder)
        define_int_var :unread_count

        # @todo Handle:
        #   <SearchParameters/>
      end

    end # SearchFolder
  end # EWS
end # Viewpoint
