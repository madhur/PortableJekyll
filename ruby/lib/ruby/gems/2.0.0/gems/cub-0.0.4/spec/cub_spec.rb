# -*- coding: utf-8 -*-
require File.expand_path(File.dirname(__FILE__) + '/spec_helper')
require 'cub'

describe Cub do
  context '証券コードに対応する会社が存在する場合' do
    it '会社名を表示' do
      Cub.company(7203).should eq('トヨタ自動車')
    end

    it '株価を表示' do
      Cub.price(7203).should be_within(1000).of(3000)
    end

    describe 'PERを表示' do
      it '連結の場合' do
        Cub.per(7203).should be > 0
      end

      it '単独の場合' do
        Cub.per(3793).should be > 0
      end
    end

    describe 'PBRを表示' do
      it '連結の場合' do
        Cub.pbr(7203).should be > 0
      end

      it '単独の場合' do
        Cub.pbr(3793).should be > 0
      end
    end
  end

  context '証券コードに対応する会社が存在しない場合' do
    it '例外を返す' do
      lambda{ Cub.company(0000) }.should raise_error(Cub::CompanyException)
      lambda{ Cub.price(0000)   }.should raise_error(Cub::CompanyException)
    end
  end

  context '証券コードが無効な場合' do
    describe '例外を返す' do
      it "#company" do
        lambda{ Cub.company(333)    }.should raise_error(Cub::CompanyException)
        lambda{ Cub.company(55555)  }.should raise_error(Cub::CompanyException)
        lambda{ Cub.company('abcd') }.should raise_error(Cub::CompanyException)
      end

      it "#price" do
        lambda{ Cub.price(333)    }.should raise_error(Cub::CompanyException)
        lambda{ Cub.price(55555)  }.should raise_error(Cub::CompanyException)
        lambda{ Cub.price('abcd') }.should raise_error(Cub::CompanyException)
      end
    end
  end
end
