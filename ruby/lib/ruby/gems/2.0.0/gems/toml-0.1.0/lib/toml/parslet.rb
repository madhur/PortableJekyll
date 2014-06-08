module TOML
  class Parslet < ::Parslet::Parser
    rule(:document) {
      all_space >>
      (table | table_array | key_value | comment_line).repeat >>
      all_space
    }
    root :document

    rule(:value) {
      array |
      string |
      datetime.as(:datetime) |
      float.as(:float) |
      integer.as(:integer) |
      boolean
    }
    
    # Finding comments in multiline arrays requires accepting a bunch of
    # possible newlines and stuff before the comment
    rule(:array_comments) { (all_space >> comment_line).repeat }
    
    rule(:array) {
      str("[") >> all_space >> array_comments >>
      ( array_comments >> # Match any comments on first line
        all_space >> value >> array_comments >>
        (
          # Separator followed by any comments
          all_space >> str(",") >> array_comments >>
          # Value followed by any comments
          all_space >> value >> array_comments
        ).repeat >>
        (all_space >> str(",")).maybe >> # possible trailing comma
        all_space >> array_comments # Grab any remaining comments just in case
      ).maybe.as(:array) >> str("]") 
    }
    
    rule(:key_value) { 
      space >> key.as(:key) >>
      space >> str("=") >>
      space >> value.as(:value) >>
      space >> comment.maybe >> str("\n") >> all_space
    }
    rule(:table) {
      space >> str("[") >>
        table_name.as(:table) >>
      str("]") >>
      space >> comment.maybe >> str("\n") >> all_space
    }
    rule(:table_array) {
      space >> str("[[") >>
        table_name.as(:table_array) >>
      str("]]") >>
      space >> comment.maybe >> str("\n") >> all_space
    }
    
    rule(:key) { match["^. \t\\]"].repeat(1) }
    rule(:table_name) { key.as(:key) >> (str(".") >> key.as(:key)).repeat }

    rule(:comment_line) { comment >> str("\n") >> all_space }
    rule(:comment) { str("#") >> match["^\n"].repeat }

    rule(:space) { match[" \t"].repeat }
    rule(:all_space) { match[" \t\r\n"].repeat }
        
    rule(:string) {
      str('"') >> (
      match["^\"\\\\"] |
      (str("\\") >> match["0tnr\"\\\\"])
      ).repeat.as(:string) >> str('"')
    }
    
    rule(:sign) { str("-") }
    rule(:sign?) { sign.maybe }
    
    rule(:integer) {
      str("0") | (sign? >> match["1-9"] >> match["0-9"].repeat)
    }
    rule(:float) {
      sign? >> match["0-9"].repeat(1) >> str(".") >> match["0-9"].repeat(1)
    }

    rule(:boolean) { str("true").as(:true) | str("false").as(:false) }
    
    rule(:date) {
      match["0-9"].repeat(4,4) >> str("-") >>
      match["0-9"].repeat(2,2) >> str("-") >>
      match["0-9"].repeat(2,2)
    }

    rule(:time) {
      match["0-9"].repeat(2,2) >> str(":") >>
      match["0-9"].repeat(2,2) >> str(":") >>
      match["0-9"].repeat(2,2)
    }

    rule(:datetime) { date >> str("T") >> time >> str("Z") }
  end
end