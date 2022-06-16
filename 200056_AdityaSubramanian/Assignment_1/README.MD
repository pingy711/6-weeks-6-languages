# Assignment 1

### Input parameters

When defining an object of class Student the constructor will require id, name, username, phone_number, dob (in ddmmyyyy format), branch, attendance (in percentage)

An example definition will be:
> aditya = Student(200056,"Aditya","adityas",1234567890,"07112002","Aerospace",75)

Similarly for defining an object of Professor you will require id, name, username, phone_number, dob (in ddmmyyyy format), field, attendance (in percentage)

An example definition will be:
> prof = Professor(12041,"Sam","sam",9087654321,"10091977","Aerofoil theory",95)

### Functions you can call

>update_info_by_id(id)

Requires your id to verify authenticity. After verification it will let you change your details.

>display_info_by_id(id)

Requires your id to verify authenticity. After verification it will display your details.

>contact_details()

Will show the *phone_number* stored in the invoking object.

>display_age()

Will show *age* stored in the invoking object.

>travel_ticket_discount(ticket_price)

Will take in the ticket price without discount as input and return the discounted fare based on the age of the member invoking it.

>attendance_is_ok()

Will return *True* of the attendance minimum has been met by the invoking member, else returns *False*.