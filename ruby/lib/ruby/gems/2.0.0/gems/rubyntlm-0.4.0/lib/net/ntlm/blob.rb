module Net
  module NTLM

    BLOB_SIGN = 0x00000101

    class Blob < FieldSet
      int32LE    :blob_signature,   {:value => BLOB_SIGN}
      int32LE    :reserved,         {:value => 0}
      int64LE    :timestamp,      {:value => 0}
      string     :challenge,      {:value => "", :size => 8}
      int32LE    :unknown1,     {:value => 0}
      string     :target_info,      {:value => "", :size => 0}
      int32LE    :unknown2,         {:value => 0}
    end

  end
end