require File.join(File.dirname(__FILE__), "..", "spec_helper")

describe SafeYAML::Transform::ToSymbol do
  def with_symbol_parsing_value(value)
    symbol_parsing_flag = YAML.enable_symbol_parsing?
    SafeYAML::OPTIONS[:enable_symbol_parsing] = value

    yield

  ensure
    SafeYAML::OPTIONS[:enable_symbol_parsing] = symbol_parsing_flag
  end

  def with_symbol_parsing(&block)
    with_symbol_parsing_value(true, &block)
  end

  def without_symbol_parsing(&block)
    with_symbol_parsing_value(false, &block)
  end

  it "returns true when the value matches a valid Symbol" do
    with_symbol_parsing { subject.transform?(":foo")[0].should be_true }
  end

  it "returns false when symbol parsing is disabled" do
    without_symbol_parsing { subject.transform?(":foo").should be_false }
  end

  it "returns false when the value does not match a valid Symbol" do
    with_symbol_parsing { subject.transform?("foo").should be_false }
  end

  it "returns false when the symbol does not begin the line" do
    with_symbol_parsing do
      subject.transform?("NOT A SYMBOL\n:foo").should be_false
    end
  end

  it "returns false when the symbol does not end the line" do
    with_symbol_parsing do
      subject.transform?(":foo\nNOT A SYMBOL").should be_false
    end
  end
end
