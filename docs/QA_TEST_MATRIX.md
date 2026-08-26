# QA Test Execution Matrix - Sprint 1
* **QA Tester:** @username
* **Client Deliverable:** Console Interactive Kiosk

| Test ID | Target Input Field | Test Input Description | Expected Output | Actual Behavior | Status (Pass/Fail) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-01 | Full Name/Test Numbers | text (`"1234"`) | ask for new name | accepts name | F |
| TC-02 | Department/Role | Blank input (`""`) | request new organization| accepted and printed blank | P |
| TC-03 | Email / Contact | Valid string (`"test@bch.org"`) | Stored & printed accurately | moves outside ascii window | F |
| TC-04 | Badge print/Ascii print |  text (`"AAAAAAAAAAAAAAAAAAAAAAA"`) | clean output on badge, make sure ascii art reshapes to fit long strings | moves outside ascii window | F |
