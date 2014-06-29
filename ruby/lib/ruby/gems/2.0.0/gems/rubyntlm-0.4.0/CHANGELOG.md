0.2.0 - Major changes to behavior!!!!
  - Bug - Type 1 packets do not include a domain and workstation by defauly. Packet capture software will see this type of packet as malformed. All packets now include this information
  - Bug - Type 3 packets do not include the calling workstation. This should be setup by default.

0.1.2
 - Feature user can specify the target domain 