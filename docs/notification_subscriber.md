# Notification_Subscriber

![Notification_Subscriber_table_img](http://www.plantuml.com/plantuml/img/0U407lz0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWJczqQMPfOs5qQMzkNrDrOdDZScbYPN8AVGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCASsjfRd1XSc5j86rlRczZQ79lRMKWT79rPGfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

## 1. Configuration

### 1.1 notification_subscriptions

**Type**: _string->uuid_ **refTable**: [Notification_Subscription](notification_subscription.html) **refType**: _strong_



List of notification subscriptions by name for this subscriber.

### 1.2 type

**Type**: _string_

Notification transport type. For WebSockets the type is "ws".

### 1.3 name

**Type**: _string_

Name of the notification subscriber.

