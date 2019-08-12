@naresh
Feature: Modify Commitement
Scenario: Validate Modify Commitement
Given Create mi order with created RQ
When Login to AXIS-O as processor and open the application
And Validate pricing information
And Re Submit MI Order with some data changes
And Login as solution center manager and open the application
And Navigate to Modify commitment in actions and make some changes to the application
Then  Validate chages in Application
