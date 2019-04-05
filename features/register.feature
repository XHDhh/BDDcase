# coding=UTF-8
Feature: Register User

  As a developer
  This is my first bdd project

  Scenario: open register website
    When I open the register website "http://www.5itest.cn/register?goto=/"
    Then I except that the title is "注册"


  Scenario: input username
    When I set with useremail "1231@qq.com"
    And I set with username "aha"
    And I set with password "12313232"
    And I set with code "test1"
    And I click with registerbutton
    Then I except that text "验证码错误"
  '''