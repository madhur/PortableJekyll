shared_examples_for 'a fieldset' do |fields|

  subject(:fieldset_class) do
    Class.new(described_class)
  end

  context 'the class' do
    it { should respond_to :string }
    it { should respond_to :int16LE }
    it { should respond_to :int32LE }
    it { should respond_to :int64LE }
    it { should respond_to :security_buffer }
    it { should respond_to :prototypes }
    it { should respond_to :names }
    it { should respond_to :types }
    it { should respond_to :opts }

    context 'adding a String Field' do
      before(:each) do
        fieldset_class.string(:test_string, { :value => 'Test'})
      end

      it 'should set the prototypes correctly' do
        fieldset_class.prototypes.should include([:test_string, Net::NTLM::String, {:value=>"Test"}])
      end

      it 'should set the names correctly' do
        fieldset_class.names.should include(:test_string)
      end

      it 'should set the types correctly' do
        fieldset_class.types.should include(Net::NTLM::String)
      end

      it 'should set the opts correctly' do
        fieldset_class.opts.should include({:value => 'Test'})
      end

      context 'when creating an instance' do
        let(:fieldset_object) do
          fieldset_class.new
        end

        it 'should have the new accessor' do
          fieldset_object.should respond_to :test_string
        end

        it 'should have the correct default value' do
          fieldset_object.test_string.should == 'Test'
        end
      end
    end

    context 'adding a Int16LE Field' do
      before(:each) do
        fieldset_class.int16LE(:test_int, { :value => 15})
      end

      it 'should set the prototypes correctly' do
        fieldset_class.prototypes.should include([:test_int, Net::NTLM::Int16LE, {:value=>15}])
      end

      it 'should set the names correctly' do
        fieldset_class.names.should include(:test_int)
      end

      it 'should set the types correctly' do
        fieldset_class.types.should include(Net::NTLM::Int16LE)
      end

      it 'should set the opts correctly' do
        fieldset_class.opts.should include({:value => 15})
      end

      context 'when creating an instance' do
        let(:fieldset_object) do
          fieldset_class.new
        end

        it 'should have the new accessor' do
          fieldset_object.should respond_to :test_int
        end

        it 'should have the correct default value' do
          fieldset_object.test_int.should == 15
        end
      end
    end

    context 'adding a Int32LE Field' do
      before(:each) do
        fieldset_class.int32LE(:test_int, { :value => 15})
      end

      it 'should set the prototypes correctly' do
        fieldset_class.prototypes.should include([:test_int, Net::NTLM::Int32LE, {:value=>15}])
      end

      it 'should set the names correctly' do
        fieldset_class.names.should include(:test_int)
      end

      it 'should set the types correctly' do
        fieldset_class.types.should include(Net::NTLM::Int32LE)
      end

      it 'should set the opts correctly' do
        fieldset_class.opts.should include({:value => 15})
      end

      context 'when creating an instance' do
        let(:fieldset_object) do
          fieldset_class.new
        end

        it 'should have the new accessor' do
          fieldset_object.should respond_to :test_int
        end

        it 'should have the correct default value' do
          fieldset_object.test_int.should == 15
        end
      end
    end

    context 'adding a Int64LE Field' do
      before(:each) do
        fieldset_class.int64LE(:test_int, { :value => 15})
      end

      it 'should set the prototypes correctly' do
        fieldset_class.prototypes.should include([:test_int, Net::NTLM::Int64LE, {:value=>15}])
      end

      it 'should set the names correctly' do
        fieldset_class.names.should include(:test_int)
      end

      it 'should set the types correctly' do
        fieldset_class.types.should include(Net::NTLM::Int64LE)
      end

      it 'should set the opts correctly' do
        fieldset_class.opts.should include({:value => 15})
      end

      context 'when creating an instance' do
        let(:fieldset_object) do
          fieldset_class.new
        end

        it 'should have the new accessor' do
          fieldset_object.should respond_to :test_int
        end

        it 'should have the correct default value' do
          fieldset_object.test_int.should == 15
        end
      end
    end

    context 'adding a SecurityBuffer Field' do
      before(:each) do
        fieldset_class.security_buffer(:test_buffer, { :value => 15})
      end

      it 'should set the prototypes correctly' do
        fieldset_class.prototypes.should include([:test_buffer, Net::NTLM::SecurityBuffer, {:value=>15}])
      end

      it 'should set the names correctly' do
        fieldset_class.names.should include(:test_buffer)
      end

      it 'should set the types correctly' do
        fieldset_class.types.should include(Net::NTLM::SecurityBuffer)
      end

      it 'should set the opts correctly' do
        fieldset_class.opts.should include({:value => 15})
      end

      context 'when creating an instance' do
        let(:fieldset_object) do
          fieldset_class.new
        end

        it 'should have the new accessor' do
          fieldset_object.should respond_to :test_buffer
        end

        it 'should have the correct default value' do
          fieldset_object.test_buffer.should == 15
        end
      end
    end

  end

  context 'an instance' do

    subject(:fieldset_object) do
      # FieldSet Base Class and Message Base Class
      # have no fields by default and thus cannot be initialized
      # currently. Clumsy workaround for now.
      if described_class.names.empty?
        described_class.string(:test_string, { :value => 'Test', :active => true, :size => 4})
      end
      described_class.new
    end

    it { should respond_to :serialize }
    it { should respond_to :parse }
    it { should respond_to :size }
    it { should respond_to :enable }
    it { should respond_to :disable }

    context 'fields' do
      fields.each do |field|
        it { should respond_to field[:name] }

        context "#{field[:name]}" do
          it "should be a #{field[:class].to_s}" do
            fieldset_object[field[:name]].class.should == field[:class]
          end

          it "should have a default value of #{field[:value]}" do
            fieldset_object[field[:name]].value.should == field[:value]
          end

          it "should have active set to #{field[:active]}" do
            fieldset_object[field[:name]].active.should == field[:active]
          end
        end
      end
    end

  end
end