I-Logix-RPY-Archive version 8.5.2 Modeler C++ 1159120
{ IProject 
	- _id = GUID 35767e1a-6028-4bab-89e6-a1087251abfc;
	- _myState = 8192;
	- _properties = { IPropertyContainer 
		- Subjects = { IRPYRawContainer 
			- size = 2;
			- value = 
			{ IPropertySubject 
				- _Name = "Activity_diagram";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "ControlFlow";
						- Properties = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IProperty 
								- _Name = "ShowName";
								- _Value = "Label";
								- _Type = Enum;
								- _ExtraTypeInfo = "Name,Label,None";
							}
							{ IProperty 
								- _Name = "ShowStereotype";
								- _Value = "None";
								- _Type = Enum;
								- _ExtraTypeInfo = "Label,Bitmap,None";
							}
							{ IProperty 
								- _Name = "line_style";
								- _Value = "spline_arrows";
								- _Type = Enum;
								- _ExtraTypeInfo = "straight_arrows,rectilinear_arrows,spline_arrows";
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "Format";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "ControlFlow";
						- Properties = { IRPYRawContainer 
							- size = 5;
							- value = 
							{ IProperty 
								- _Name = "Font.Font";
								- _Value = "Arial";
								- _Type = String;
							}
							{ IProperty 
								- _Name = "Font.FontColor";
								- _Value = "0,0,255";
								- _Type = Color;
							}
							{ IProperty 
								- _Name = "Font.Size";
								- _Value = "10";
								- _Type = Int;
							}
							{ IProperty 
								- _Name = "Line.LineColor";
								- _Value = "221,0,0";
								- _Type = Color;
							}
							{ IProperty 
								- _Name = "Line.LineWidth";
								- _Value = "1";
								- _Type = Int;
							}
						}
					}
				}
			}
		}
	}
	- _name = "Team_Project_Calendar";
	- _objectCreation = "32568731735202520-21921953";
	- _umlDependencyID = "3795";
	- _lastID = 10;
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _filename = "Default.sbs";
		- _subsystem = "";
		- _class = "";
		- _name = "Default";
		- _id = GUID 8ab0fde4-735d-49e2-ba05-80f58a789e9c;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _filename = "DefaultComponent.cmp";
		- _subsystem = "";
		- _class = "";
		- _name = "DefaultComponent";
		- _id = GUID eb8cc07c-afdf-48cd-a213-09a012030068;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = -1;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ ISubsystem 
			- fileName = "Default";
			- _id = GUID 8ab0fde4-735d-49e2-ba05-80f58a789e9c;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IDiagram 
			- _id = GUID 3e0e416b-cfbd-45bc-b9d4-976338e2816b;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 4;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Association";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Class";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,34,84,148";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "ControlFlow";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Inheritance";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,16,230";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Domain Diagram";
			- _objectCreation = "32568751735202520-21922153";
			- _umlDependencyID = "2981";
			- _lastModifiedTime = "5.15.2025::1:32:1";
			- _graphicChart = { CGIClassChart 
				- _id = GUID ab5b25f7-0af1-4bd7-abee-d7d4082c82e6;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID 3e0e416b-cfbd-45bc-b9d4-976338e2816b;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 8;
				{ CGIClass 
					- _id = GUID f8a29019-933e-4b68-9f0a-2c6e3f35f691;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID 40c63d4c-48a3-4efa-b80b-c395387a36d3;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID c21c940c-cd92-4710-94e4-7b1fdffcda5a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "User";
						- _id = GUID 4cf3efd0-6e29-483e-8429-ddf6e1f309e8;
					}
					- m_pParent = GUID f8a29019-933e-4b68-9f0a-2c6e3f35f691;
					- m_name = { CGIText 
						- m_str = "User";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2088;
					- m_transform = 0.236072 0 0 0.656863 476.527 -137.108 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "username";
							- _id = GUID 94bc352e-3f9f-4a31-bbdf-1452100ce87c;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "password";
							- _id = GUID a3af7a8f-67d9-4e9f-82ee-2ae1c6972e2e;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "accountType";
							- _id = GUID 80fdb50b-75ad-43ee-a73c-7a5bdc354ab7;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 19;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "getAccountType()";
							- _id = GUID c9fee85d-3c55-4f8f-bb17-8ced8835d5a3;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "getUserID()";
							- _id = GUID 0aa80016-da57-4023-b878-29eca86442a9;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "displaySuccessMessage()";
							- _id = GUID 300458aa-8630-4e69-90b7-52b427d62574;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "requestEventInfo()";
							- _id = GUID 75e6a368-a50c-4736-98ef-4ece99e88c19;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "getPasswordFromDB()";
							- _id = GUID e1d6d8b7-0536-47c3-8fc5-b32ae8f75951;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "checkUsernameExistsInDB()";
							- _id = GUID 4d42e0b6-d086-46e0-ad32-0416903ad3d2;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "getAccountTypeFromDB()";
							- _id = GUID 359c513e-e8b4-4fc1-a986-178a6efd0fe8;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "logIn()";
							- _id = GUID eb0a1af8-3eab-4921-a68e-bb6d3a4becdf;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "setUsername()";
							- _id = GUID 9c75681e-3cb5-4008-b080-03bc6ed1b8b6;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "setPassword()";
							- _id = GUID 44900e2b-d5fa-4ec6-b9f6-3557549488ef;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "addEvent()";
							- _id = GUID d83a8c9d-36f6-4957-bdad-ce82c7a6f14c;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "deleteEvent()";
							- _id = GUID 37418a7d-fb7a-4c27-a99b-26f27bba1661;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "deleteEventFromDB()";
							- _id = GUID 8e649723-e953-4d0a-8e4f-baea73d1601a;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "editEvent()";
							- _id = GUID 519f6ecb-53aa-4d18-8f40-4ccface3069e;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "validateEvent()";
							- _id = GUID 1ce6ffb2-2c1c-425e-b6b3-5a00732117b2;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "editEventInDB()";
							- _id = GUID e96037b7-f1cc-4b03-b7bf-37dd8df8670b;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "createAccount()";
							- _id = GUID 78220f29-573c-485d-9e1b-8cfcef06ab18;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "confirmPassword()";
							- _id = GUID b10c8c58-5caf-407e-a749-53813178ae11;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "addCredentialsToDB()";
							- _id = GUID abdfb474-fee8-4aaf-a9d6-cf1f893b812d;
						}
					}
				}
				{ CGIClass 
					- _id = GUID bef8bf7a-7078-4a1d-be79-5816390565b7;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Event";
						- _id = GUID 38070086-3a95-4dc1-907b-0c75c7de6b2e;
					}
					- m_pParent = GUID f8a29019-933e-4b68-9f0a-2c6e3f35f691;
					- m_name = { CGIText 
						- m_str = "Event";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.220963 0 0 0.311052 865.558 111.664 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 8;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "eventType";
							- _id = GUID 6ee2cadd-f74d-4608-b6e8-00bdeb356d22;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "eventCreatorID";
							- _id = GUID 6bf51d6d-18b3-492b-b007-4d1cddbfa353;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "eventID";
							- _id = GUID 0a54c997-67a5-465d-9e6b-7f0bec9c5f5d;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "eventDate";
							- _id = GUID 99e32ca8-c43e-48cd-aa75-dca3ef4af5b4;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "eventTime";
							- _id = GUID cf361c75-98cd-461c-8714-4fc1819ddb5f;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "eventLength";
							- _id = GUID 68d9e013-cc56-4bb1-9154-df7173c85be7;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "eventName";
							- _id = GUID 296b6731-762d-430c-8b9b-6eb385ac6721;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "eventDescription";
							- _id = GUID 89346913-f1ce-438e-aac1-9fe505fa4ef6;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 5;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "saveToDatabase()";
							- _id = GUID 7e7b47e8-e753-44a1-9fd2-adff1c746e6d;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "getEventCreatorID()";
							- _id = GUID 02feeb75-5bc7-4d58-b9b5-337549b65094;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "getEventType()";
							- _id = GUID 35d2f18c-ec11-48cc-a07e-6859f7e5984a;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "getEventInfo()";
							- _id = GUID d2a2ce26-6d78-4bd6-b5e6-c2bbae1107b5;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "checkEventOverlaps()";
							- _id = GUID 3b04e3f6-59e5-408d-a5e0-8cfad0b41341;
						}
					}
				}
				{ CGIAssociationEnd 
					- _id = GUID 4aabe9f3-e138-479d-8a7a-9a4ac1287638;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "User";
						- _name = "itsEvent_1";
						- _id = GUID a60c97cf-863b-4f24-844d-ec6a2c378259;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID c21c940c-cd92-4710-94e4-7b1fdffcda5a;
					- m_sourceType = 'F';
					- m_pTarget = GUID bef8bf7a-7078-4a1d-be79-5816390565b7;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 951 819 ;
					- m_TargetPort = 292 930 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Event";
						- _name = "itsUser_1";
						- _id = GUID 7033314d-9ac3-44ab-860b-68daa0262494;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "1..*";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "0..*";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIClass 
					- _id = GUID bd6a289c-29f9-42db-985a-ef2048ca763a;
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Manager";
						- _id = GUID cbd7fc63-5706-4077-a062-06f87361209d;
					}
					- m_pParent = GUID f8a29019-933e-4b68-9f0a-2c6e3f35f691;
					- m_name = { CGIText 
						- m_str = "Manager";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.213409 0 0 0.334225 190.573 91.0401 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Manager";
							- _name = "scheduleMeeting()";
							- _id = GUID 1e0d4c5f-dcda-41c4-aef9-30199b3d0c63;
						}
					}
				}
				{ CGIInheritance 
					- _id = GUID 56495a58-d5a4-4e89-bb4c-70ade6eaea66;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "User";
						- _name = "Manager";
						- _id = GUID 3e53f55f-f36f-4d0f-925f-07cd552d610e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID c21c940c-cd92-4710-94e4-7b1fdffcda5a;
					- m_sourceType = 'F';
					- m_pTarget = GUID bd6a289c-29f9-42db-985a-ef2048ca763a;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 142 792 ;
					- m_TargetPort = 897 868 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID 49a76b6a-8b54-4ee0-b18d-bb8c74c7872e;
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "GroupMeeting";
						- _id = GUID baaf2c16-aa04-4645-874d-9442dbe5a359;
					}
					- m_pParent = GUID f8a29019-933e-4b68-9f0a-2c6e3f35f691;
					- m_name = { CGIText 
						- m_str = "GroupMeeting";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.230406 0 0 0.311943 1150.54 106.371 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "GroupMeeting";
							- _name = "eventAttendees";
							- _id = GUID d4f90382-d291-4f90-9ec0-70e03b077a44;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "GroupMeeting";
							- _name = "retrieveAttendees()";
							- _id = GUID f8779a1f-1659-4b95-8da3-e814153d79b4;
						}
					}
				}
				{ CGIInheritance 
					- _id = GUID 8effddb8-fbbf-4d21-9d83-99f30dfc6055;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Event";
						- _name = "GroupMeeting";
						- _id = GUID 491455cf-694a-4a65-be79-03a42d2c4a55;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID bef8bf7a-7078-4a1d-be79-5816390565b7;
					- m_sourceType = 'F';
					- m_pTarget = GUID 49a76b6a-8b54-4ee0-b18d-bb8c74c7872e;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 975 882 ;
					- m_TargetPort = 158 896 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID f8a29019-933e-4b68-9f0a-2c6e3f35f691;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID 8ab0fde4-735d-49e2-ba05-80f58a789e9c;
			}
		}
	}
	- MSCS = { IRPYRawContainer 
		- size = 7;
		- value = 
		{ IMSC 
			- _id = GUID e99e3747-4c0e-4d92-9abb-ee7a3597b814;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 8;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "CombinedFragment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,250,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "ControlFlow";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "CreateMessage";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InstanceLine";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,96,437";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InteractionOperand";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,100,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Fill.Transparent_Fill";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Message";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "ReplyMessage";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "execution_occurrence";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "SequenceDiagram";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "General";
								- Properties = { IRPYRawContainer 
									- size = 3;
									- value = 
									{ IProperty 
										- _Name = "ClassCentricMode";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "CleanupRealized";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "RealizeMessages";
										- _Value = "True";
										- _Type = Bool;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Add Event";
			- _objectCreation = "32568771735202520-21922353";
			- _umlDependencyID = "2471";
			- _lastModifiedTime = "4.27.2025::0:54:11";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 20;
				- m_usingActivationBar = 0;
				- _id = GUID 86e722d0-f108-465a-8a50-826a82b6f44a;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IMSC";
					- _id = GUID e99e3747-4c0e-4d92-9abb-ee7a3597b814;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 11;
				{ CGIBox 
					- _id = GUID 5169d831-71de-400e-882b-0b8fab055f2e;
					- m_type = 108;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID 81a59e62-3e08-456e-980a-975e5300157c;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "opt";
					- _id = GUID 3e421ba1-8af8-4f69-8b77-06f86977136c;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID 3d58bddc-7c8a-45b6-a7e3-3ccc6ab0b1bb;
					}
					- m_pParent = GUID 5169d831-71de-400e-882b-0b8fab055f2e;
					- m_name = { CGIText 
						- m_str = "interactionOperator_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.669725 0 0 1 195.055 0 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 527 244  854 244  854 377  527 377  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=133>
<frame Id=GUID 669757fe-3b15-41eb-adba-9a95955e03e2>";
				}
				{ CGIMscColumnCR 
					- _id = GUID bf486312-4862-4c6c-83da-27aaf0f701c8;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 0e4ab33e-2f42-4b7d-811d-babaec42e8e1;
					}
					- m_pParent = GUID 5169d831-71de-400e-882b-0b8fab055f2e;
					- m_name = { CGIText 
						- m_str = ":Event";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.00849957 551 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 656fdc38-411e-4e19-80e4-62300bca6691;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 3c0c4275-b478-46d5-a714-1f95aa343c9f;
					}
					- m_pParent = GUID 5169d831-71de-400e-882b-0b8fab055f2e;
					- m_name = { CGIText 
						- m_str = ":User";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.00849957 184 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID cc74cf3c-2f6c-499f-8212-0183f9eba486;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID fd8805b9-23ad-4500-8683-0e5e063ca6de;
					}
					- m_pParent = GUID bf486312-4862-4c6c-83da-27aaf0f701c8;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 519.634 42 17883.3 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID b16b631e-bd15-4abd-9dcb-9b1ec599bcf3;
				}
				{ CGIMscMessage 
					- _id = GUID c0da5763-6182-4073-8942-76c9a861a1f2;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 04b926d4-82de-4e20-bd2a-51d7d1e338d2;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "overlapsExist=checkEventOverlaps(eventTime, eventLength)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 656fdc38-411e-4e19-80e4-62300bca6691;
					- m_sourceType = 'F';
					- m_pTarget = GUID bf486312-4862-4c6c-83da-27aaf0f701c8;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 21531 ;
					- m_TargetPort = 48 21531 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID b16b631e-bd15-4abd-9dcb-9b1ec599bcf3;
					- m_type = 112;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 9e5a9431-cde6-41b1-8ac3-140d5c4135b4;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Event(*args[eventTime, eventLength, etc.])";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 656fdc38-411e-4e19-80e4-62300bca6691;
					- m_sourceType = 'F';
					- m_pTarget = GUID bf486312-4862-4c6c-83da-27aaf0f701c8;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 17883 ;
					- m_TargetPort = 48 17883 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID cc74cf3c-2f6c-499f-8212-0183f9eba486;
				}
				{ CGIMscMessage 
					- _id = GUID 88552ced-a30b-47a9-86a1-0b1e9794fee3;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 9115cfee-d4b6-4945-8b95-06f091c5033e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "saveToDatabase()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID bf486312-4862-4c6c-83da-27aaf0f701c8;
					- m_sourceType = 'F';
					- m_pTarget = GUID bf486312-4862-4c6c-83da-27aaf0f701c8;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 624 308  624 347  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 30354 ;
					- m_TargetPort = 48 34943 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID e95d2a28-65b3-466c-b286-b8418b7f6506;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 4dff63ec-0769-4c66-a919-d898933601f3;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "addEvent(*args)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 656fdc38-411e-4e19-80e4-62300bca6691;
					- m_sourceType = 'F';
					- m_pTarget = GUID 656fdc38-411e-4e19-80e4-62300bca6691;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 262 131  262 163  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 9530 ;
					- m_TargetPort = 48 13295 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 9901ce86-31e1-45d4-8c02-788519135aa7;
				}
				{ CGIMscInteractionOperand 
					- _id = GUID 669757fe-3b15-41eb-adba-9a95955e03e2;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID 7f5bdc1b-9660-42ff-a386-dcf2d5d97c42;
					}
					- m_pParent = GUID 3e421ba1-8af8-4f69-8b77-06f86977136c;
					- m_name = { CGIText 
						- m_str = "overlapsExist==False";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -18 -30  136 -30  136 -12  -18 -12  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 626 277 ;
						- m_nHorizontalSpacing = 28;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 527 244  854 244  854 377  527 377  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 9901ce86-31e1-45d4-8c02-788519135aa7;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID c4daaf75-b459-401a-a791-8814cc514623;
					}
					- m_pParent = GUID 656fdc38-411e-4e19-80e4-62300bca6691;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 294.133 42 13294.8 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID e95d2a28-65b3-466c-b286-b8418b7f6506;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 5169d831-71de-400e-882b-0b8fab055f2e;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID 8ab0fde4-735d-49e2-ba05-80f58a789e9c;
			}
			- m_pICollaboration = { ICollaboration 
				- _id = GUID 81a59e62-3e08-456e-980a-975e5300157c;
				- _objectCreation = "32568791735202520-21922553";
				- _umlDependencyID = "1696";
				- ClassifierRoles = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IClassifierRole 
						- _id = GUID 0e4ab33e-2f42-4b7d-811d-babaec42e8e1;
						- _myState = 2048;
						- _objectCreation = "32568811735202520-21922753";
						- _umlDependencyID = "1691";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Event";
							- _id = GUID 38070086-3a95-4dc1-907b-0c75c7de6b2e;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 3c0c4275-b478-46d5-a714-1f95aa343c9f;
						- _myState = 2048;
						- _objectCreation = "32568831735202520-21922953";
						- _umlDependencyID = "1695";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "User";
							- _id = GUID 4cf3efd0-6e29-483e-8429-ddf6e1f309e8;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- Messages = { IRPYRawContainer 
					- size = 4;
					- value = 
					{ IMessage 
						- _id = GUID 9115cfee-d4b6-4945-8b95-06f091c5033e;
						- _name = "saveToDatabase";
						- _objectCreation = "32568851735202520-21923153";
						- _umlDependencyID = "3105";
						- m_szSequence = "4.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 0e4ab33e-2f42-4b7d-811d-babaec42e8e1;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 0e4ab33e-2f42-4b7d-811d-babaec42e8e1;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "saveToDatabase()";
							- _id = GUID 7e7b47e8-e753-44a1-9fd2-adff1c746e6d;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 9e5a9431-cde6-41b1-8ac3-140d5c4135b4;
						- _myState = 8192;
						- _name = "Event";
						- _objectCreation = "32568871735202520-21923353";
						- _umlDependencyID = "2208";
						- m_szSequence = "2.";
						- m_szActualArgs = "*args[eventTime, eventLength, etc.]";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 0e4ab33e-2f42-4b7d-811d-babaec42e8e1;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 3c0c4275-b478-46d5-a714-1f95aa343c9f;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CREATE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID fd8805b9-23ad-4500-8683-0e5e063ca6de;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 04b926d4-82de-4e20-bd2a-51d7d1e338d2;
						- _myState = 8192;
						- _name = "checkEventOverlaps";
						- _objectCreation = "32568891735202520-21923553";
						- _umlDependencyID = "3566";
						- m_szSequence = "3.";
						- m_szActualArgs = "eventTime, eventLength";
						- m_szReturnVal = "overlapsExist";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 0e4ab33e-2f42-4b7d-811d-babaec42e8e1;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 3c0c4275-b478-46d5-a714-1f95aa343c9f;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "checkEventOverlaps()";
							- _id = GUID 3b04e3f6-59e5-408d-a5e0-8cfad0b41341;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 4dff63ec-0769-4c66-a919-d898933601f3;
						- _myState = 8192;
						- _name = "addEvent";
						- _objectCreation = "32568911735202520-21923753";
						- _umlDependencyID = "2504";
						- m_szSequence = "1.";
						- m_szActualArgs = "*args";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 3c0c4275-b478-46d5-a714-1f95aa343c9f;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 3c0c4275-b478-46d5-a714-1f95aa343c9f;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "addEvent()";
							- _id = GUID d83a8c9d-36f6-4957-bdad-ce82c7a6f14c;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID c4daaf75-b459-401a-a791-8814cc514623;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- ExecutionOccurrences = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IExecutionOccurrence 
						- _id = GUID fd8805b9-23ad-4500-8683-0e5e063ca6de;
						- _objectCreation = "32568931735202520-21923953";
						- _umlDependencyID = "1697";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 9e5a9431-cde6-41b1-8ac3-140d5c4135b4;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 159;
					}
					{ IExecutionOccurrence 
						- _id = GUID c4daaf75-b459-401a-a791-8814cc514623;
						- _objectCreation = "32568951735202520-21924153";
						- _umlDependencyID = "1692";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 4dff63ec-0769-4c66-a919-d898933601f3;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 90;
					}
				}
				- CombinedFragments = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ ICombinedFragment 
						- _id = GUID 3d58bddc-7c8a-45b6-a7e3-3ccc6ab0b1bb;
						- _myState = 2048;
						- _name = "interactionOperator_0";
						- _objectCreation = "32568971735202520-21924353";
						- _umlDependencyID = "3867";
						- _interactionOperator = "opt";
						- InteractionOperands = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IInteractionOperand 
								- _id = GUID 7f5bdc1b-9660-42ff-a386-dcf2d5d97c42;
								- _myState = 2048;
								- _name = "interactionOperand_0";
								- _objectCreation = "32568991735202520-21924553";
								- _umlDependencyID = "3740";
								- _interactionConstraint = "overlapsExist==False";
							}
						}
					}
				}
			}
		}
		{ IMSC 
			- _id = GUID 316f0acd-81c0-4e2b-b061-7528efee3ae1;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 8;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "CombinedFragment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,250,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "ControlFlow";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "CreateMessage";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InstanceLine";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,96,437";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InteractionOperand";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,100,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Fill.Transparent_Fill";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Message";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "ReplyMessage";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "execution_occurrence";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "SequenceDiagram";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "General";
								- Properties = { IRPYRawContainer 
									- size = 3;
									- value = 
									{ IProperty 
										- _Name = "ClassCentricMode";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "CleanupRealized";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "RealizeMessages";
										- _Value = "True";
										- _Type = Bool;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Delete Personal Event";
			- _objectCreation = "32569011735202520-21924753";
			- _umlDependencyID = "3631";
			- _lastModifiedTime = "4.27.2025::0:54:11";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 20;
				- m_usingActivationBar = 0;
				- _id = GUID f06a0979-e1c2-4884-af6e-b19b6d2da5d7;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IMSC";
					- _id = GUID 316f0acd-81c0-4e2b-b061-7528efee3ae1;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 11;
				{ CGIBox 
					- _id = GUID 1011b04c-2f6a-4c46-80b8-46d2488157f8;
					- m_type = 108;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID e79bf0b4-751b-4b7d-ae81-5aa8872a8b9c;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "opt";
					- _id = GUID e78a2480-9eee-41a2-b862-3226d5e6f62b;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID ff84d73d-7c16-455c-b26c-88da6caadf39;
					}
					- m_pParent = GUID 1011b04c-2f6a-4c46-80b8-46d2488157f8;
					- m_name = { CGIText 
						- m_str = "interactionOperator_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.987952 0 0 1 -215.494 63 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 623 280  872 280  872 405  623 405  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=125>
<frame Id=GUID 107deb28-73db-46fd-b734-66c8f96681b4>";
				}
				{ CGIMscColumnCR 
					- _id = GUID daa112a4-69dd-43fa-a493-76e27a4241a9;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 3bf35728-2ea8-44ec-b00d-e9d73d032059;
					}
					- m_pParent = GUID 1011b04c-2f6a-4c46-80b8-46d2488157f8;
					- m_name = { CGIText 
						- m_str = ":User";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0112459 397 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 9009e8e7-062f-48e9-95b4-6b34555376e3;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID d265e941-6918-411d-8018-7eb54779b7c6;
					}
					- m_pParent = GUID 1011b04c-2f6a-4c46-80b8-46d2488157f8;
					- m_name = { CGIText 
						- m_str = ":Event";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0112459 627 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 303a2f0d-eadb-458c-a4bb-b6c7b7ba889d;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 1e82f004-9a4e-44f6-a632-54c03df0dc74;
					}
					- m_pParent = GUID 9009e8e7-062f-48e9-95b4-6b34555376e3;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 125.972 42 16628.3 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID cc3dba7a-1fe0-4c27-9749-0d692e82647c;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 093d955a-b824-4b7d-857b-f3c4091db0cd;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 38c4ed09-5e9b-4c30-970d-79b300c0e02b;
					}
					- m_pParent = GUID daa112a4-69dd-43fa-a493-76e27a4241a9;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 649.621 42 11293 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID b767ecf7-4213-49c3-8fe9-251098b11852;
				}
				{ CGIMscMessage 
					- _id = GUID 29f5f67d-a56f-4a15-a2be-1bc27c3d0d57;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID d9d33ede-9b11-4149-b873-e679dbd6a78b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "deleteEventFromDB(eventID)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID daa112a4-69dd-43fa-a493-76e27a4241a9;
					- m_sourceType = 'F';
					- m_pTarget = GUID daa112a4-69dd-43fa-a493-76e27a4241a9;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 475 390  475 428  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 30233 ;
					- m_TargetPort = 48 33612 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 23feee62-1c90-4cfa-9a4c-726ce922ce00;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 9a077072-07ca-40aa-bd0f-b3341fae481c;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "eventType=getEventType(eventID)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID daa112a4-69dd-43fa-a493-76e27a4241a9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 9009e8e7-062f-48e9-95b4-6b34555376e3;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 19029 ;
					- m_TargetPort = 48 19029 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID b767ecf7-4213-49c3-8fe9-251098b11852;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 8d107511-e26c-4b98-838a-ba0f6e2ed207;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "deleteEvent(eventID)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID daa112a4-69dd-43fa-a493-76e27a4241a9;
					- m_sourceType = 'F';
					- m_pTarget = GUID daa112a4-69dd-43fa-a493-76e27a4241a9;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 475 136  475 177  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 7647 ;
					- m_TargetPort = 48 11293 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 093d955a-b824-4b7d-857b-f3c4091db0cd;
				}
				{ CGIMscMessage 
					- _id = GUID cc3dba7a-1fe0-4c27-9749-0d692e82647c;
					- m_type = 112;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 65fe1b0a-3903-4725-b7b8-86b699afd958;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Event(eventID)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID daa112a4-69dd-43fa-a493-76e27a4241a9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 9009e8e7-062f-48e9-95b4-6b34555376e3;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 16628 ;
					- m_TargetPort = 48 16628 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 303a2f0d-eadb-458c-a4bb-b6c7b7ba889d;
				}
				{ CGIMscInteractionOperand 
					- _id = GUID 107deb28-73db-46fd-b734-66c8f96681b4;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID 308d7447-484e-4654-a1e2-04fef4c1bae7;
					}
					- m_pParent = GUID e78a2480-9eee-41a2-b862-3226d5e6f62b;
					- m_name = { CGIText 
						- m_str = "eventType==\"personal\"";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 623 280  872 280  872 405  623 405  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 1011b04c-2f6a-4c46-80b8-46d2488157f8;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID 8ab0fde4-735d-49e2-ba05-80f58a789e9c;
			}
			- m_pICollaboration = { ICollaboration 
				- _id = GUID e79bf0b4-751b-4b7d-ae81-5aa8872a8b9c;
				- _objectCreation = "32569031735202520-21924953";
				- _umlDependencyID = "1690";
				- ClassifierRoles = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IClassifierRole 
						- _id = GUID 3bf35728-2ea8-44ec-b00d-e9d73d032059;
						- _myState = 2048;
						- _objectCreation = "32569051735202520-21925153";
						- _umlDependencyID = "1685";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "User";
							- _id = GUID 4cf3efd0-6e29-483e-8429-ddf6e1f309e8;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID d265e941-6918-411d-8018-7eb54779b7c6;
						- _myState = 2048;
						- _objectCreation = "32569071735202520-21925353";
						- _umlDependencyID = "1689";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Event";
							- _id = GUID 38070086-3a95-4dc1-907b-0c75c7de6b2e;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- Messages = { IRPYRawContainer 
					- size = 4;
					- value = 
					{ IMessage 
						- _id = GUID 9a077072-07ca-40aa-bd0f-b3341fae481c;
						- _myState = 8192;
						- _name = "getEventType";
						- _objectCreation = "32569091735202520-21925553";
						- _umlDependencyID = "2945";
						- m_szSequence = "3.";
						- m_szActualArgs = "eventID";
						- m_szReturnVal = "eventType";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d265e941-6918-411d-8018-7eb54779b7c6;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 3bf35728-2ea8-44ec-b00d-e9d73d032059;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "getEventType()";
							- _id = GUID 35d2f18c-ec11-48cc-a07e-6859f7e5984a;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID d9d33ede-9b11-4149-b873-e679dbd6a78b;
						- _myState = 8192;
						- _name = "deleteEventFromDB";
						- _objectCreation = "32569111735202520-21925753";
						- _umlDependencyID = "3367";
						- m_szSequence = "4.";
						- m_szActualArgs = "eventID";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 3bf35728-2ea8-44ec-b00d-e9d73d032059;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 3bf35728-2ea8-44ec-b00d-e9d73d032059;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "deleteEventFromDB()";
							- _id = GUID 8e649723-e953-4d0a-8e4f-baea73d1601a;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 65fe1b0a-3903-4725-b7b8-86b699afd958;
						- _myState = 8192;
						- _name = "Event";
						- _objectCreation = "32569131735202520-21925953";
						- _umlDependencyID = "2206";
						- m_szSequence = "2.";
						- m_szActualArgs = "eventID";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d265e941-6918-411d-8018-7eb54779b7c6;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 3bf35728-2ea8-44ec-b00d-e9d73d032059;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CREATE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 1e82f004-9a4e-44f6-a632-54c03df0dc74;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 8d107511-e26c-4b98-838a-ba0f6e2ed207;
						- _myState = 8192;
						- _name = "deleteEvent";
						- _objectCreation = "32569151735202520-21926153";
						- _umlDependencyID = "2828";
						- m_szSequence = "1.";
						- m_szActualArgs = "eventID";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 3bf35728-2ea8-44ec-b00d-e9d73d032059;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 3bf35728-2ea8-44ec-b00d-e9d73d032059;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "deleteEvent()";
							- _id = GUID 37418a7d-fb7a-4c27-a99b-26f27bba1661;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 38c4ed09-5e9b-4c30-970d-79b300c0e02b;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- ExecutionOccurrences = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IExecutionOccurrence 
						- _id = GUID 1e82f004-9a4e-44f6-a632-54c03df0dc74;
						- _objectCreation = "32569171735202520-21926353";
						- _umlDependencyID = "1691";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 65fe1b0a-3903-4725-b7b8-86b699afd958;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 51;
					}
					{ IExecutionOccurrence 
						- _id = GUID 38c4ed09-5e9b-4c30-970d-79b300c0e02b;
						- _objectCreation = "32569191735202520-21926553";
						- _umlDependencyID = "1695";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 8d107511-e26c-4b98-838a-ba0f6e2ed207;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 263;
					}
				}
				- CombinedFragments = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ ICombinedFragment 
						- _id = GUID ff84d73d-7c16-455c-b26c-88da6caadf39;
						- _myState = 2048;
						- _name = "interactionOperator_0";
						- _objectCreation = "32569211735202520-21926753";
						- _umlDependencyID = "3861";
						- _interactionOperator = "opt";
						- InteractionOperands = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IInteractionOperand 
								- _id = GUID 308d7447-484e-4654-a1e2-04fef4c1bae7;
								- _myState = 2048;
								- _name = "interactionOperand_0";
								- _objectCreation = "32569231735202520-21926953";
								- _umlDependencyID = "3734";
								- _interactionConstraint = "eventType==\"personal\"";
							}
						}
					}
				}
			}
		}
		{ IMSC 
			- _id = GUID b9d3a814-2c29-453c-a86a-a31555854728;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 8;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "CombinedFragment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,250,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "ControlFlow";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "CreateMessage";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InstanceLine";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,96,437";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InteractionOperand";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,100,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Fill.Transparent_Fill";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Message";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "ReplyMessage";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "execution_occurrence";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "SequenceDiagram";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "General";
								- Properties = { IRPYRawContainer 
									- size = 3;
									- value = 
									{ IProperty 
										- _Name = "ClassCentricMode";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "CleanupRealized";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "RealizeMessages";
										- _Value = "True";
										- _Type = Bool;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Delete Group Event";
			- _objectCreation = "32569251735202520-21927153";
			- _umlDependencyID = "3323";
			- _lastModifiedTime = "4.27.2025::0:54:11";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 20;
				- m_usingActivationBar = 0;
				- _id = GUID a51a202f-6732-49a7-8537-300b31d5804a;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IMSC";
					- _id = GUID b9d3a814-2c29-453c-a86a-a31555854728;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 14;
				{ CGIBox 
					- _id = GUID 56e7633f-8ceb-4970-a5d2-1030e121d448;
					- m_type = 108;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID 2c287e25-55c4-4739-8092-2cc7e7f79481;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "opt";
					- _id = GUID 6c335dc7-41ff-430c-8313-a5a508e24c4c;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID 757bf7ba-55cb-4c02-8d09-da8e03bc4855;
					}
					- m_pParent = GUID 56e7633f-8ceb-4970-a5d2-1030e121d448;
					- m_name = { CGIText 
						- m_str = "interactionOperator_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.893229 0 0 1 75.487 0 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 323 242  707 242  707 339  323 339  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=97>
<frame Id=GUID f1e594b6-bfe0-4364-b972-976224d0ea6f>";
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "opt";
					- _id = GUID dd4ad2a2-0dad-491a-b174-71d91572f896;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID 64ee8c10-b7e3-49c0-9225-4d0c74701e5e;
					}
					- m_pParent = GUID 56e7633f-8ceb-4970-a5d2-1030e121d448;
					- m_name = { CGIText 
						- m_str = "interactionOperator_1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.764574 0 0 1 109.926 -147 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 331 503  777 503  777 606  331 606  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=103>
<frame Id=GUID 3f2e13f6-9d49-42fa-a7b8-f66222946944>";
				}
				{ CGIMscColumnCR 
					- _id = GUID 791b9727-dcd6-46e0-8f4f-240fa1547b66;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 97065f22-2ef4-4de1-988a-e2a567e98309;
					}
					- m_pParent = GUID 56e7633f-8ceb-4970-a5d2-1030e121d448;
					- m_name = { CGIText 
						- m_str = ":User";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0102035 369 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID e7e7db62-226a-46d2-98f8-0b101e5e9717;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID a2155bc2-07fe-48f7-ba48-49211fd41657;
					}
					- m_pParent = GUID 56e7633f-8ceb-4970-a5d2-1030e121d448;
					- m_name = { CGIText 
						- m_str = ":Event";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0102035 619 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 1f23ce9a-75ec-40a4-a4d0-c6c6acedcd66;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 75cc2844-3321-4e7b-b618-b6a92c83baa0;
					}
					- m_pParent = GUID e7e7db62-226a-46d2-98f8-0b101e5e9717;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 307.63 42 14504.9 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 78f802f2-f78a-4765-a4c6-39fe8f98a18f;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 77f4de51-444f-4c26-949c-22d9850c83b9;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID d5358ca5-92a2-4034-8b21-28971fa77fe7;
					}
					- m_pParent = GUID 791b9727-dcd6-46e0-8f4f-240fa1547b66;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 745.933 42 12152.7 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID c6362e45-480f-432b-980c-170f9f7bbde9;
				}
				{ CGIMscMessage 
					- _id = GUID 18cfc983-14ed-4f20-bb7e-75ba0e268d9b;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 182ba52a-3597-4957-b501-3560420d2a1f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "eventCreatorID=getEventCreatorID()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 791b9727-dcd6-46e0-8f4f-240fa1547b66;
					- m_sourceType = 'F';
					- m_pTarget = GUID e7e7db62-226a-46d2-98f8-0b101e5e9717;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 23619 ;
					- m_TargetPort = 48 23619 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 78f802f2-f78a-4765-a4c6-39fe8f98a18f;
					- m_type = 112;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 53abc2a8-afef-4cf7-b2d0-ed8af7e18835;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Event(eventID)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 791b9727-dcd6-46e0-8f4f-240fa1547b66;
					- m_sourceType = 'F';
					- m_pTarget = GUID e7e7db62-226a-46d2-98f8-0b101e5e9717;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 14505 ;
					- m_TargetPort = 48 14505 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 1f23ce9a-75ec-40a4-a4d0-c6c6acedcd66;
				}
				{ CGIMscMessage 
					- _id = GUID d5bbdf04-5e08-48be-af34-beb49f3054b2;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 951f0112-cf3b-4e1a-8e09-f43e58b1e766;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "deleteEventFromDB(eventID)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 791b9727-dcd6-46e0-8f4f-240fa1547b66;
					- m_sourceType = 'F';
					- m_pTarget = GUID 791b9727-dcd6-46e0-8f4f-240fa1547b66;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 442 413  442 438  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 35576 ;
					- m_TargetPort = 48 38026 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 5ea3f0d1-8508-438d-a620-2c32e27e6164;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID d7324963-f160-41d0-aab8-ae7877f787bf;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "eventType=getEventType()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 791b9727-dcd6-46e0-8f4f-240fa1547b66;
					- m_sourceType = 'F';
					- m_pTarget = GUID e7e7db62-226a-46d2-98f8-0b101e5e9717;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 17445 ;
					- m_TargetPort = 48 17445 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID c6362e45-480f-432b-980c-170f9f7bbde9;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 93183514-b5ff-40d4-89c3-c2ef583dff3e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "deleteEvent(eventID)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 791b9727-dcd6-46e0-8f4f-240fa1547b66;
					- m_sourceType = 'F';
					- m_pTarget = GUID 791b9727-dcd6-46e0-8f4f-240fa1547b66;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 440 138  440 174  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 8625 ;
					- m_TargetPort = 48 12153 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 77f4de51-444f-4c26-949c-22d9850c83b9;
				}
				{ CGIMscInteractionOperand 
					- _id = GUID f1e594b6-bfe0-4364-b972-976224d0ea6f;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID 5f41dd7f-7be7-4178-b8b3-b0c827dc7290;
					}
					- m_pParent = GUID 6c335dc7-41ff-430c-8313-a5a508e24c4c;
					- m_name = { CGIText 
						- m_str = "eventType==\"group\"";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -26 -23  127 -23  127 -5  -26 -5  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 485 269 ;
						- m_nHorizontalSpacing = 20;
						- m_nVerticalSpacing = 4;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 323 242  707 242  707 339  323 339  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIMscInteractionOperand 
					- _id = GUID 3f2e13f6-9d49-42fa-a7b8-f66222946944;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID 4fff61de-400c-4a75-8842-8d5edf362662;
					}
					- m_pParent = GUID dd4ad2a2-0dad-491a-b174-71d91572f896;
					- m_name = { CGIText 
						- m_str = "User.accountType==\"manager\"&
eventCreatorID=User.uID";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 12 -57  238 -57  238 -21  12 -21  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 415 436 ;
						- m_nHorizontalSpacing = 23;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 331 503  777 503  777 606  331 606  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 56e7633f-8ceb-4970-a5d2-1030e121d448;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID 8ab0fde4-735d-49e2-ba05-80f58a789e9c;
			}
			- m_pICollaboration = { ICollaboration 
				- _id = GUID 2c287e25-55c4-4739-8092-2cc7e7f79481;
				- _objectCreation = "32569271735202520-21927353";
				- _umlDependencyID = "1693";
				- ClassifierRoles = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IClassifierRole 
						- _id = GUID 97065f22-2ef4-4de1-988a-e2a567e98309;
						- _myState = 2048;
						- _objectCreation = "32569291735202520-21927553";
						- _umlDependencyID = "1697";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "User";
							- _id = GUID 4cf3efd0-6e29-483e-8429-ddf6e1f309e8;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID a2155bc2-07fe-48f7-ba48-49211fd41657;
						- _myState = 2048;
						- _objectCreation = "32569311735202520-21927753";
						- _umlDependencyID = "1692";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Event";
							- _id = GUID 38070086-3a95-4dc1-907b-0c75c7de6b2e;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- Messages = { IRPYRawContainer 
					- size = 5;
					- value = 
					{ IMessage 
						- _id = GUID d7324963-f160-41d0-aab8-ae7877f787bf;
						- _myState = 8192;
						- _name = "getEventType";
						- _objectCreation = "32569331735202520-21927953";
						- _umlDependencyID = "2948";
						- m_szSequence = "3.";
						- m_szActualArgs = "";
						- m_szReturnVal = "eventType";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID a2155bc2-07fe-48f7-ba48-49211fd41657;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 97065f22-2ef4-4de1-988a-e2a567e98309;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "getEventType()";
							- _id = GUID 35d2f18c-ec11-48cc-a07e-6859f7e5984a;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 93183514-b5ff-40d4-89c3-c2ef583dff3e;
						- _myState = 8192;
						- _name = "deleteEvent";
						- _objectCreation = "32569351735202520-21928153";
						- _umlDependencyID = "2832";
						- m_szSequence = "1.";
						- m_szActualArgs = "eventID";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 97065f22-2ef4-4de1-988a-e2a567e98309;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 97065f22-2ef4-4de1-988a-e2a567e98309;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "deleteEvent()";
							- _id = GUID 37418a7d-fb7a-4c27-a99b-26f27bba1661;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID d5358ca5-92a2-4034-8b21-28971fa77fe7;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 182ba52a-3597-4957-b501-3560420d2a1f;
						- _name = "getEventCreatorID";
						- _objectCreation = "32569371735202520-21928353";
						- _umlDependencyID = "3390";
						- m_szSequence = "4.";
						- m_szActualArgs = "";
						- m_szReturnVal = "eventCreatorID";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID a2155bc2-07fe-48f7-ba48-49211fd41657;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 97065f22-2ef4-4de1-988a-e2a567e98309;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "getEventCreatorID()";
							- _id = GUID 02feeb75-5bc7-4d58-b9b5-337549b65094;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 951f0112-cf3b-4e1a-8e09-f43e58b1e766;
						- _myState = 8192;
						- _name = "deleteEventFromDB";
						- _objectCreation = "32569391735202520-21928553";
						- _umlDependencyID = "3378";
						- m_szSequence = "5.";
						- m_szActualArgs = "eventID";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 97065f22-2ef4-4de1-988a-e2a567e98309;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 97065f22-2ef4-4de1-988a-e2a567e98309;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "deleteEventFromDB()";
							- _id = GUID 8e649723-e953-4d0a-8e4f-baea73d1601a;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 53abc2a8-afef-4cf7-b2d0-ed8af7e18835;
						- _myState = 8192;
						- _name = "Event";
						- _objectCreation = "32569411735202520-21928753";
						- _umlDependencyID = "2208";
						- m_szSequence = "2.";
						- m_szActualArgs = "eventID";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID a2155bc2-07fe-48f7-ba48-49211fd41657;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 97065f22-2ef4-4de1-988a-e2a567e98309;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CREATE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 75cc2844-3321-4e7b-b618-b6a92c83baa0;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- ExecutionOccurrences = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IExecutionOccurrence 
						- _id = GUID d5358ca5-92a2-4034-8b21-28971fa77fe7;
						- _objectCreation = "32569431735202520-21928953";
						- _umlDependencyID = "1698";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 93183514-b5ff-40d4-89c3-c2ef583dff3e;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 274;
					}
					{ IExecutionOccurrence 
						- _id = GUID 75cc2844-3321-4e7b-b618-b6a92c83baa0;
						- _objectCreation = "32569451735202520-21929153";
						- _umlDependencyID = "1693";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 53abc2a8-afef-4cf7-b2d0-ed8af7e18835;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 113;
					}
				}
				- CombinedFragments = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ ICombinedFragment 
						- _id = GUID 757bf7ba-55cb-4c02-8d09-da8e03bc4855;
						- _myState = 2048;
						- _name = "interactionOperator_0";
						- _objectCreation = "32569471735202520-21929353";
						- _umlDependencyID = "3868";
						- _interactionOperator = "opt";
						- InteractionOperands = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IInteractionOperand 
								- _id = GUID 5f41dd7f-7be7-4178-b8b3-b0c827dc7290;
								- _myState = 2048;
								- _name = "interactionOperand_0";
								- _objectCreation = "32569491735202520-21929553";
								- _umlDependencyID = "3741";
								- _interactionConstraint = "eventType==\"group\"";
							}
						}
					}
					{ ICombinedFragment 
						- _id = GUID 64ee8c10-b7e3-49c0-9225-4d0c74701e5e;
						- _myState = 2048;
						- _name = "interactionOperator_1";
						- _objectCreation = "32569511735202520-21929753";
						- _umlDependencyID = "3868";
						- _interactionOperator = "opt";
						- InteractionOperands = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IInteractionOperand 
								- _id = GUID 4fff61de-400c-4a75-8842-8d5edf362662;
								- _myState = 2048;
								- _name = "interactionOperand_0";
								- _objectCreation = "32569531735202520-21929953";
								- _umlDependencyID = "3740";
								- _interactionConstraint = "User.accountType==\"manager\"&
eventCreatorID=User.uID";
							}
						}
					}
				}
			}
		}
		{ IMSC 
			- _id = GUID e1958c64-8270-47aa-94b0-300d8e9b2903;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 8;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "CombinedFragment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,250,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "ControlFlow";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "CreateMessage";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InstanceLine";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,96,437";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InteractionOccurrence";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,216,134";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,16,230";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InteractionOperand";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,100,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Fill.Transparent_Fill";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Message";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "execution_occurrence";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "SequenceDiagram";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "General";
								- Properties = { IRPYRawContainer 
									- size = 3;
									- value = 
									{ IProperty 
										- _Name = "ClassCentricMode";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "CleanupRealized";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "RealizeMessages";
										- _Value = "True";
										- _Type = Bool;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Edit Personal Event";
			- _objectCreation = "32569551735202520-21930153";
			- _umlDependencyID = "3426";
			- _lastModifiedTime = "4.27.2025::0:54:11";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 16;
				- m_usingActivationBar = 0;
				- _id = GUID 5b845110-c6be-4c70-880e-9edd448d73a0;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IMSC";
					- _id = GUID e1958c64-8270-47aa-94b0-300d8e9b2903;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 16;
				{ CGIBox 
					- _id = GUID 4ba2f57e-29b1-4031-a358-bb77145e9748;
					- m_type = 108;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID 834848fb-339e-467b-9499-66274fe45788;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "opt";
					- _id = GUID 856f4b63-5d95-4505-afe8-b9816703abae;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID 57dbe64f-8120-4f80-8330-0231aeb60750;
					}
					- m_pParent = GUID 4ba2f57e-29b1-4031-a358-bb77145e9748;
					- m_name = { CGIText 
						- m_str = "interactionOperator_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.637747 0 0 1 165.912 0 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 458 219  1115 219  1115 362  458 362  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=143>
<frame Id=GUID d6bb3e86-4ba3-4f57-83f4-b6420319fe04>";
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "opt";
					- _id = GUID 02b22219-a684-4152-9053-45d07aa1da7c;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID 880e30f1-99ae-4a33-8c69-a61da9b035af;
					}
					- m_pParent = GUID 4ba2f57e-29b1-4031-a358-bb77145e9748;
					- m_name = { CGIText 
						- m_str = "interactionOperator_1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.868613 0 0 1 -145.555 1 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 696 372  970 372  970 470  696 470  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=98>
<frame Id=GUID c4be22c8-90df-4344-a00b-11e689e27154>";
				}
				{ CGIMscColumnCR 
					- _id = GUID 4993c5bb-662b-4c6f-bdc4-ed665ea85bbe;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 21465f52-8578-4b42-a689-b8dc2add4adb;
					}
					- m_pParent = GUID 4ba2f57e-29b1-4031-a358-bb77145e9748;
					- m_name = { CGIText 
						- m_str = ":User";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0102837 454 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 021efd5b-3567-483e-99af-4a9d798027d8;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 7e2ed26c-e0ae-439c-bab1-ed138241f6b1;
					}
					- m_pParent = GUID 4ba2f57e-29b1-4031-a358-bb77145e9748;
					- m_name = { CGIText 
						- m_str = ":Event";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0102837 785 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID cfe13928-e46b-4472-891c-e1bbf9d5dcab;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 0967368b-f7be-4352-8d4a-7cad1ff7b50c;
					}
					- m_pParent = GUID 021efd5b-3567-483e-99af-4a9d798027d8;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 302.53 42 10696.6 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 8f3d7133-7b83-433c-8818-243b913ae138;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 28e8ee6a-1d96-4f35-af47-67b22e481ec9;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID effe1a96-f920-4d2a-9692-62b5810b1b68;
					}
					- m_pParent = GUID 4993c5bb-662b-4c6f-bdc4-ed665ea85bbe;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 880.578 42 8362.79 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 98e068df-c413-4b8d-a2ae-1bcda146d6bd;
				}
				{ CGIMscMessage 
					- _id = GUID 8f3d7133-7b83-433c-8818-243b913ae138;
					- m_type = 112;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 7b838dbb-9e4f-4751-8d20-1b2aa6edca8c;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Event(eventID)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4993c5bb-662b-4c6f-bdc4-ed665ea85bbe;
					- m_sourceType = 'F';
					- m_pTarget = GUID 021efd5b-3567-483e-99af-4a9d798027d8;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 10697 ;
					- m_TargetPort = 48 10697 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID cfe13928-e46b-4472-891c-e1bbf9d5dcab;
				}
				{ CGIMscMessage 
					- _id = GUID 40a4d582-e0a2-485a-a64c-1daf2a4ea2c3;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 5cb30e4c-7034-4d63-a743-718a95173c01;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "newEventInfoValidated=validateEvent(newEventInfo)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4993c5bb-662b-4c6f-bdc4-ed665ea85bbe;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4993c5bb-662b-4c6f-bdc4-ed665ea85bbe;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 531 323  531 352  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 26547 ;
					- m_TargetPort = 48 29367 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 7533ef14-f72d-4ebb-bd4e-a42fe87f7c61;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 46ca5946-a380-4f68-83e0-de08e04ad09e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "eventInfo=getEventInfo()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4993c5bb-662b-4c6f-bdc4-ed665ea85bbe;
					- m_sourceType = 'F';
					- m_pTarget = GUID 021efd5b-3567-483e-99af-4a9d798027d8;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 20032 ;
					- m_TargetPort = 48 20032 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 98e068df-c413-4b8d-a2ae-1bcda146d6bd;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID e6d71f8c-b9b6-4807-aded-8a2bace72e67;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "editEvent(eventID)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4993c5bb-662b-4c6f-bdc4-ed665ea85bbe;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4993c5bb-662b-4c6f-bdc4-ed665ea85bbe;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 531 120  531 136  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 6807 ;
					- m_TargetPort = 48 8363 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 28e8ee6a-1d96-4f35-af47-67b22e481ec9;
				}
				{ CGIMscMessage 
					- _id = GUID 06448126-92d8-4a1b-a4e6-cec2d1430d58;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 24045e59-4286-4dc4-9110-e10d709d689f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "editEventInDB(newEventInfo)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4993c5bb-662b-4c6f-bdc4-ed665ea85bbe;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4993c5bb-662b-4c6f-bdc4-ed665ea85bbe;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 532 417  532 445  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 35688 ;
					- m_TargetPort = 48 38410 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID d2c1add0-df87-4f01-b45a-aee90376ad38;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID db1c4cb2-d0f9-44a5-9ace-5939c5eb8378;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "newEventInfo=requestEventInfo(eventInfo)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4993c5bb-662b-4c6f-bdc4-ed665ea85bbe;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4993c5bb-662b-4c6f-bdc4-ed665ea85bbe;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 534 278  534 305  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 22171 ;
					- m_TargetPort = 48 24797 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 5b39e240-31ce-42e7-9d1a-ed17cf315dc6;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID eb01efd5-8ba2-48ad-9eed-299805957178;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "eventType=getEventType(eventID)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4993c5bb-662b-4c6f-bdc4-ed665ea85bbe;
					- m_sourceType = 'F';
					- m_pTarget = GUID 021efd5b-3567-483e-99af-4a9d798027d8;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 13906 ;
					- m_TargetPort = 48 13906 ;
					- m_bLeft = 0;
				}
				{ CGIMscInteractionOperand 
					- _id = GUID d6bb3e86-4ba3-4f57-83f4-b6420319fe04;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID 23e3db3b-3b3b-4c47-b949-de38cfa54da6;
					}
					- m_pParent = GUID 856f4b63-5d95-4505-afe8-b9816703abae;
					- m_name = { CGIText 
						- m_str = "eventType==\"personal\"";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  165 -9  165 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 591 230 ;
						- m_nHorizontalSpacing = 3;
						- m_nVerticalSpacing = 2;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 458 219  1115 219  1115 362  458 362  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIMscInteractionOperand 
					- _id = GUID c4be22c8-90df-4344-a00b-11e689e27154;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID fa19b738-0dcf-41b6-8d3d-415809acb522;
					}
					- m_pParent = GUID 02b22219-a684-4152-9053-45d07aa1da7c;
					- m_name = { CGIText 
						- m_str = "newEventInfoValidated==True";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -48 -16  142 -16  142 2  -48 2  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 809 365 ;
						- m_nHorizontalSpacing = 23;
						- m_nVerticalSpacing = 2;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 696 372  970 372  970 470  696 470  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 4ba2f57e-29b1-4031-a358-bb77145e9748;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID 8ab0fde4-735d-49e2-ba05-80f58a789e9c;
			}
			- m_pICollaboration = { ICollaboration 
				- _id = GUID 834848fb-339e-467b-9499-66274fe45788;
				- _objectCreation = "32569571735202520-21930353";
				- _umlDependencyID = "1690";
				- ClassifierRoles = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IClassifierRole 
						- _id = GUID 21465f52-8578-4b42-a689-b8dc2add4adb;
						- _myState = 2048;
						- _objectCreation = "32569591735202520-21930553";
						- _umlDependencyID = "1694";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "User";
							- _id = GUID 4cf3efd0-6e29-483e-8429-ddf6e1f309e8;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 7e2ed26c-e0ae-439c-bab1-ed138241f6b1;
						- _myState = 2048;
						- _objectCreation = "32569611735202520-21930753";
						- _umlDependencyID = "1689";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Event";
							- _id = GUID 38070086-3a95-4dc1-907b-0c75c7de6b2e;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- Messages = { IRPYRawContainer 
					- size = 7;
					- value = 
					{ IMessage 
						- _id = GUID 24045e59-4286-4dc4-9110-e10d709d689f;
						- _myState = 8192;
						- _name = "editEventInDB";
						- _objectCreation = "32569631735202520-21930953";
						- _umlDependencyID = "2946";
						- m_szSequence = "7.";
						- m_szActualArgs = "newEventInfo";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 21465f52-8578-4b42-a689-b8dc2add4adb;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 21465f52-8578-4b42-a689-b8dc2add4adb;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "editEventInDB()";
							- _id = GUID e96037b7-f1cc-4b03-b7bf-37dd8df8670b;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID e6d71f8c-b9b6-4807-aded-8a2bace72e67;
						- _myState = 8192;
						- _name = "editEvent";
						- _objectCreation = "32569651735202520-21931153";
						- _umlDependencyID = "2624";
						- m_szSequence = "1.";
						- m_szActualArgs = "eventID";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 21465f52-8578-4b42-a689-b8dc2add4adb;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 21465f52-8578-4b42-a689-b8dc2add4adb;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "editEvent()";
							- _id = GUID 519f6ecb-53aa-4d18-8f40-4ccface3069e;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID effe1a96-f920-4d2a-9692-62b5810b1b68;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 7b838dbb-9e4f-4751-8d20-1b2aa6edca8c;
						- _myState = 8192;
						- _name = "Event";
						- _objectCreation = "32569671735202520-21931353";
						- _umlDependencyID = "2206";
						- m_szSequence = "2.";
						- m_szActualArgs = "eventID";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 7e2ed26c-e0ae-439c-bab1-ed138241f6b1;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 21465f52-8578-4b42-a689-b8dc2add4adb;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CREATE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 0967368b-f7be-4352-8d4a-7cad1ff7b50c;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID eb01efd5-8ba2-48ad-9eed-299805957178;
						- _myState = 8192;
						- _name = "getEventType";
						- _objectCreation = "32569691735202520-21931553";
						- _umlDependencyID = "2948";
						- m_szSequence = "3.";
						- m_szActualArgs = "eventID";
						- m_szReturnVal = "eventType";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 7e2ed26c-e0ae-439c-bab1-ed138241f6b1;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 21465f52-8578-4b42-a689-b8dc2add4adb;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "getEventType()";
							- _id = GUID 35d2f18c-ec11-48cc-a07e-6859f7e5984a;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID db1c4cb2-d0f9-44a5-9ace-5939c5eb8378;
						- _myState = 8192;
						- _name = "requestEventInfo";
						- _objectCreation = "32569711735202520-21931753";
						- _umlDependencyID = "3378";
						- m_szSequence = "5.";
						- m_szActualArgs = "eventInfo";
						- m_szReturnVal = "newEventInfo";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 21465f52-8578-4b42-a689-b8dc2add4adb;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 21465f52-8578-4b42-a689-b8dc2add4adb;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "requestEventInfo()";
							- _id = GUID 75e6a368-a50c-4736-98ef-4ece99e88c19;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 46ca5946-a380-4f68-83e0-de08e04ad09e;
						- _name = "getEventInfo";
						- _objectCreation = "32569731735202520-21931953";
						- _umlDependencyID = "2925";
						- m_szSequence = "4.";
						- m_szActualArgs = "";
						- m_szReturnVal = "eventInfo";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 7e2ed26c-e0ae-439c-bab1-ed138241f6b1;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 21465f52-8578-4b42-a689-b8dc2add4adb;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "getEventInfo()";
							- _id = GUID d2a2ce26-6d78-4bd6-b5e6-c2bbae1107b5;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 5cb30e4c-7034-4d63-a743-718a95173c01;
						- _myState = 8192;
						- _name = "validateEvent";
						- _objectCreation = "32569751735202520-21932153";
						- _umlDependencyID = "3046";
						- m_szSequence = "6.";
						- m_szActualArgs = "newEventInfo";
						- m_szReturnVal = "newEventInfoValidated";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 21465f52-8578-4b42-a689-b8dc2add4adb;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 21465f52-8578-4b42-a689-b8dc2add4adb;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "validateEvent()";
							- _id = GUID 1ce6ffb2-2c1c-425e-b6b3-5a00732117b2;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- ExecutionOccurrences = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IExecutionOccurrence 
						- _id = GUID effe1a96-f920-4d2a-9692-62b5810b1b68;
						- _objectCreation = "32569771735202520-21932353";
						- _umlDependencyID = "1694";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID e6d71f8c-b9b6-4807-aded-8a2bace72e67;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 326;
					}
					{ IExecutionOccurrence 
						- _id = GUID 0967368b-f7be-4352-8d4a-7cad1ff7b50c;
						- _objectCreation = "32569791735202520-21932553";
						- _umlDependencyID = "1698";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 7b838dbb-9e4f-4751-8d20-1b2aa6edca8c;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 112;
					}
				}
				- CombinedFragments = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ ICombinedFragment 
						- _id = GUID 57dbe64f-8120-4f80-8330-0231aeb60750;
						- _myState = 2048;
						- _name = "interactionOperator_0";
						- _objectCreation = "32569811735202520-21932753";
						- _umlDependencyID = "3864";
						- _interactionOperator = "opt";
						- InteractionOperands = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IInteractionOperand 
								- _id = GUID 23e3db3b-3b3b-4c47-b949-de38cfa54da6;
								- _myState = 2048;
								- _name = "interactionOperand_0";
								- _objectCreation = "32569831735202520-21932953";
								- _umlDependencyID = "3737";
								- _interactionConstraint = "eventType==\"personal\"";
							}
						}
					}
					{ ICombinedFragment 
						- _id = GUID 880e30f1-99ae-4a33-8c69-a61da9b035af;
						- _myState = 2048;
						- _name = "interactionOperator_1";
						- _objectCreation = "32569851735202520-21933153";
						- _umlDependencyID = "3864";
						- _interactionOperator = "opt";
						- InteractionOperands = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IInteractionOperand 
								- _id = GUID fa19b738-0dcf-41b6-8d3d-415809acb522;
								- _myState = 2048;
								- _name = "interactionOperand_0";
								- _objectCreation = "32569871735202520-21933353";
								- _umlDependencyID = "3736";
								- _interactionConstraint = "newEventInfoValidated==True";
							}
						}
					}
				}
			}
		}
		{ IMSC 
			- _id = GUID e90aabe1-54a9-4684-a37f-9992f0ba6da4;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 7;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "CombinedFragment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,250,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "ControlFlow";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "CreateMessage";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InstanceLine";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,96,437";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InteractionOperand";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,100,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Fill.Transparent_Fill";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Message";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "execution_occurrence";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Edit Group Event";
			- _objectCreation = "32569891735202520-21933553";
			- _umlDependencyID = "3129";
			- _lastModifiedTime = "4.27.2025::0:54:11";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 20;
				- m_usingActivationBar = 0;
				- _id = GUID d95f7ddb-6445-4a4f-b749-d260eac73aea;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IMSC";
					- _id = GUID e90aabe1-54a9-4684-a37f-9992f0ba6da4;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 19;
				{ CGIBox 
					- _id = GUID 785bba48-6bd8-43cc-8b2d-1970cbad4012;
					- m_type = 108;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID 3cfee32d-78af-4dff-b3c4-76834377e29f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "opt";
					- _id = GUID f951027c-e881-442f-b698-3e31cd71a990;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID d84c194d-97a9-4ccf-b5b5-6f203b31d1bf;
					}
					- m_pParent = GUID 785bba48-6bd8-43cc-8b2d-1970cbad4012;
					- m_name = { CGIText 
						- m_str = "interactionOperator_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.616588 0 0 1 -12.8575 -24 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 329 239  968 239  968 355  329 355  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=116>
<frame Id=GUID f01ab230-39f7-4db1-bf65-83db44ce5012>";
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "opt";
					- _id = GUID 042ced9a-73c2-4d77-9135-bbf87002cc21;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID c1d69640-da38-434c-a3c9-1c71fcb38b68;
					}
					- m_pParent = GUID 785bba48-6bd8-43cc-8b2d-1970cbad4012;
					- m_name = { CGIText 
						- m_str = "interactionOperator_1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.10056 0 0 1 -19.3073 0 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 192 367  550 367  550 529  192 529  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=162>
<frame Id=GUID d74f83eb-65a4-40ae-9739-2156c734a903>";
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "opt";
					- _id = GUID cc4ba653-fb86-4971-b862-172da6c59a4d;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID 8be8ebfa-6f2e-4772-81f1-b213fd764644;
					}
					- m_pParent = GUID 785bba48-6bd8-43cc-8b2d-1970cbad4012;
					- m_name = { CGIText 
						- m_str = "interactionOperator_2";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.05839 0 0 1 -266.226 42 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 432 507  706 507  706 601  432 601  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=94>
<frame Id=GUID 5c4e5910-8565-4b29-b1da-3ee82f9944e0>";
				}
				{ CGIMscColumnCR 
					- _id = GUID c11c87e2-31f7-4f9d-ab1e-20554e57c71f;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 94afbbd3-8ff0-4a37-a158-c2ac27d16af6;
					}
					- m_pParent = GUID 785bba48-6bd8-43cc-8b2d-1970cbad4012;
					- m_name = { CGIText 
						- m_str = ":User";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0138519 202 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID ce6a9bfa-ecf5-478f-9e59-0eab3481342f;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 13b5c053-f03c-4940-80aa-7d723d1b3ad0;
					}
					- m_pParent = GUID 785bba48-6bd8-43cc-8b2d-1970cbad4012;
					- m_name = { CGIText 
						- m_str = ":Event";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0138519 493 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID b09183ea-7cf6-4c7d-ba1c-071e490e0457;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 44d005d1-8bf9-48d0-8103-b897f3d185d7;
					}
					- m_pParent = GUID ce6a9bfa-ecf5-478f-9e59-0eab3481342f;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 553.475 42 8590.89 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 9ed1ce8a-9d54-471f-bb60-ebb2f1a2a03f;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 8ffa3f76-d7e8-4ea2-9525-0565bf50d028;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID f1415668-6dfc-45ae-9197-76447732c223;
					}
					- m_pParent = GUID c11c87e2-31f7-4f9d-ab1e-20554e57c71f;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 958.554 42 7002.66 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 23da1baf-ce89-4123-9447-b5e5ccccd4b6;
				}
				{ CGIMscMessage 
					- _id = GUID 3487cb7d-7800-44a0-841e-427964c5fcd2;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 154d4753-9cde-4558-bcd2-455a14b5ee21;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "eventType=getEventType()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID c11c87e2-31f7-4f9d-ab1e-20554e57c71f;
					- m_sourceType = 'F';
					- m_pTarget = GUID ce6a9bfa-ecf5-478f-9e59-0eab3481342f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 10829 ;
					- m_TargetPort = 48 10829 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 9ed1ce8a-9d54-471f-bb60-ebb2f1a2a03f;
					- m_type = 112;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID e7317f97-6a4d-4e50-a030-b9602fbb8c2b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Event(eventID)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID c11c87e2-31f7-4f9d-ab1e-20554e57c71f;
					- m_sourceType = 'F';
					- m_pTarget = GUID ce6a9bfa-ecf5-478f-9e59-0eab3481342f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 8591 ;
					- m_TargetPort = 48 8591 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID b09183ea-7cf6-4c7d-ba1c-071e490e0457;
				}
				{ CGIMscMessage 
					- _id = GUID a38f0051-4aff-43f2-8769-4447a53ddd80;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 8141a614-c6ea-4707-a5f8-5e4384aea205;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "newEventInfo=requestEventInfo()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID c11c87e2-31f7-4f9d-ab1e-20554e57c71f;
					- m_sourceType = 'F';
					- m_pTarget = GUID c11c87e2-31f7-4f9d-ab1e-20554e57c71f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 280 445  280 464  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 28516 ;
					- m_TargetPort = 48 29888 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 23da1baf-ce89-4123-9447-b5e5ccccd4b6;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID b424c1f8-5d4d-41c2-b9b3-5bf18f1f876b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "editEvent(eventID)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID c11c87e2-31f7-4f9d-ab1e-20554e57c71f;
					- m_sourceType = 'F';
					- m_pTarget = GUID c11c87e2-31f7-4f9d-ab1e-20554e57c71f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 280 128  280 147  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 5631 ;
					- m_TargetPort = 48 7003 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 8ffa3f76-d7e8-4ea2-9525-0565bf50d028;
				}
				{ CGIMscMessage 
					- _id = GUID 0adfc7b3-20d0-4679-aeb2-a65a6892af9b;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID d91fe6ba-5779-47e7-920c-ad94dc468c9a;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "eventCreatorID=getEventCreatorID()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID c11c87e2-31f7-4f9d-ab1e-20554e57c71f;
					- m_sourceType = 'F';
					- m_pTarget = GUID ce6a9bfa-ecf5-478f-9e59-0eab3481342f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 16893 ;
					- m_TargetPort = 48 16893 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 5bba6b36-aa96-4875-adb6-989997fd3b37;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 18694ff4-cffa-4b5c-ae1b-534a9e6d5983;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "eventInfoValidated=validateEvent(newEventInfo)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID c11c87e2-31f7-4f9d-ab1e-20554e57c71f;
					- m_sourceType = 'F';
					- m_pTarget = GUID c11c87e2-31f7-4f9d-ab1e-20554e57c71f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 280 488  280 507  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 31620 ;
					- m_TargetPort = 48 32992 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 8adde031-103f-4119-8336-50465b9de62c;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID a9e76fa2-596a-4ddb-83d4-ac6a48d7b5a5;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "eventInfo=getEventInfo()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID c11c87e2-31f7-4f9d-ab1e-20554e57c71f;
					- m_sourceType = 'F';
					- m_pTarget = GUID ce6a9bfa-ecf5-478f-9e59-0eab3481342f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 26783 ;
					- m_TargetPort = 48 26783 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 0f27c243-3732-4bb3-aa3d-264c3351f674;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID d77742de-7048-41aa-9972-dd10f11758f7;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "editEventInDB(newEventInfo)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID c11c87e2-31f7-4f9d-ab1e-20554e57c71f;
					- m_sourceType = 'F';
					- m_pTarget = GUID c11c87e2-31f7-4f9d-ab1e-20554e57c71f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 281 600  281 620  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 39706 ;
					- m_TargetPort = 48 41150 ;
					- m_bLeft = 0;
				}
				{ CGIMscInteractionOperand 
					- _id = GUID f01ab230-39f7-4db1-bf65-83db44ce5012;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID 95df5a2f-5590-4fa9-8c8d-bdac520a47b8;
					}
					- m_pParent = GUID f951027c-e881-442f-b698-3e31cd71a990;
					- m_name = { CGIText 
						- m_str = "eventType==\"group\"";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  147 -9  147 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 1;
						- m_transform = 1 0 0 0.888889 293 226 ;
						- m_nHorizontalSpacing = -6;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 329 239  968 239  968 355  329 355  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIMscInteractionOperand 
					- _id = GUID d74f83eb-65a4-40ae-9739-2156c734a903;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID 68d98946-22ce-402c-aec8-982d15280512;
					}
					- m_pParent = GUID 042ced9a-73c2-4d77-9135-bbf87002cc21;
					- m_name = { CGIText 
						- m_str = "User.accountType==\"manager\"&
eventCreatorID=User.uID";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  343 -9  343 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 1;
						- m_transform = 1 0 0 1.83333 205 386.5 ;
						- m_nHorizontalSpacing = 2;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 192 367  550 367  550 529  192 529  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIMscInteractionOperand 
					- _id = GUID 5c4e5910-8565-4b29-b1da-3ee82f9944e0;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID edfff77c-30cf-4432-8299-6899ccaf7e07;
					}
					- m_pParent = GUID cc4ba653-fb86-4971-b862-172da6c59a4d;
					- m_name = { CGIText 
						- m_str = "eventInfoValidated==True";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -48 -16  142 -16  142 2  -48 2  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 566 501 ;
						- m_nHorizontalSpacing = 19;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 432 507  706 507  706 601  432 601  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 785bba48-6bd8-43cc-8b2d-1970cbad4012;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID 8ab0fde4-735d-49e2-ba05-80f58a789e9c;
			}
			- m_pICollaboration = { ICollaboration 
				- _id = GUID 3cfee32d-78af-4dff-b3c4-76834377e29f;
				- _objectCreation = "32569911735202520-21933753";
				- _umlDependencyID = "1695";
				- ClassifierRoles = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IClassifierRole 
						- _id = GUID 94afbbd3-8ff0-4a37-a158-c2ac27d16af6;
						- _myState = 2048;
						- _objectCreation = "32569931735202520-21933953";
						- _umlDependencyID = "1699";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "User";
							- _id = GUID 4cf3efd0-6e29-483e-8429-ddf6e1f309e8;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 13b5c053-f03c-4940-80aa-7d723d1b3ad0;
						- _myState = 2048;
						- _objectCreation = "32569951735202520-21934153";
						- _umlDependencyID = "1694";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Event";
							- _id = GUID 38070086-3a95-4dc1-907b-0c75c7de6b2e;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- Messages = { IRPYRawContainer 
					- size = 8;
					- value = 
					{ IMessage 
						- _id = GUID d77742de-7048-41aa-9972-dd10f11758f7;
						- _myState = 8192;
						- _name = "editEventInDB";
						- _objectCreation = "32569971735202520-21934353";
						- _umlDependencyID = "2951";
						- m_szSequence = "8.";
						- m_szActualArgs = "newEventInfo";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 94afbbd3-8ff0-4a37-a158-c2ac27d16af6;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 94afbbd3-8ff0-4a37-a158-c2ac27d16af6;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "editEventInDB()";
							- _id = GUID e96037b7-f1cc-4b03-b7bf-37dd8df8670b;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID b424c1f8-5d4d-41c2-b9b3-5bf18f1f876b;
						- _myState = 8192;
						- _name = "editEvent";
						- _objectCreation = "32569991735202520-21934553";
						- _umlDependencyID = "2638";
						- m_szSequence = "1.";
						- m_szActualArgs = "eventID";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 94afbbd3-8ff0-4a37-a158-c2ac27d16af6;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 94afbbd3-8ff0-4a37-a158-c2ac27d16af6;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "editEvent()";
							- _id = GUID 519f6ecb-53aa-4d18-8f40-4ccface3069e;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID f1415668-6dfc-45ae-9197-76447732c223;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID d91fe6ba-5779-47e7-920c-ad94dc468c9a;
						- _name = "getEventCreatorID";
						- _objectCreation = "32570011735202520-21934753";
						- _umlDependencyID = "3374";
						- m_szSequence = "4.";
						- m_szActualArgs = "";
						- m_szReturnVal = "eventCreatorID";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 13b5c053-f03c-4940-80aa-7d723d1b3ad0;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 94afbbd3-8ff0-4a37-a158-c2ac27d16af6;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "getEventCreatorID()";
							- _id = GUID 02feeb75-5bc7-4d58-b9b5-337549b65094;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 154d4753-9cde-4558-bcd2-455a14b5ee21;
						- _myState = 8192;
						- _name = "getEventType";
						- _objectCreation = "32570031735202520-21934953";
						- _umlDependencyID = "2935";
						- m_szSequence = "3.";
						- m_szActualArgs = "";
						- m_szReturnVal = "eventType";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 13b5c053-f03c-4940-80aa-7d723d1b3ad0;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 94afbbd3-8ff0-4a37-a158-c2ac27d16af6;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "getEventType()";
							- _id = GUID 35d2f18c-ec11-48cc-a07e-6859f7e5984a;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID e7317f97-6a4d-4e50-a030-b9602fbb8c2b;
						- _myState = 8192;
						- _name = "Event";
						- _objectCreation = "32570051735202520-21935153";
						- _umlDependencyID = "2192";
						- m_szSequence = "2.";
						- m_szActualArgs = "eventID";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 13b5c053-f03c-4940-80aa-7d723d1b3ad0;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 94afbbd3-8ff0-4a37-a158-c2ac27d16af6;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CREATE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 44d005d1-8bf9-48d0-8103-b897f3d185d7;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID a9e76fa2-596a-4ddb-83d4-ac6a48d7b5a5;
						- _name = "getEventInfo";
						- _objectCreation = "32570071735202520-21935353";
						- _umlDependencyID = "2912";
						- m_szSequence = "5.";
						- m_szActualArgs = "";
						- m_szReturnVal = "eventInfo";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 13b5c053-f03c-4940-80aa-7d723d1b3ad0;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 94afbbd3-8ff0-4a37-a158-c2ac27d16af6;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Event";
							- _name = "getEventInfo()";
							- _id = GUID d2a2ce26-6d78-4bd6-b5e6-c2bbae1107b5;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 8141a614-c6ea-4707-a5f8-5e4384aea205;
						- _name = "requestEventInfo";
						- _objectCreation = "32570091735202520-21935553";
						- _umlDependencyID = "3373";
						- m_szSequence = "6.";
						- m_szActualArgs = "";
						- m_szReturnVal = "newEventInfo";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 94afbbd3-8ff0-4a37-a158-c2ac27d16af6;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 94afbbd3-8ff0-4a37-a158-c2ac27d16af6;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "requestEventInfo()";
							- _id = GUID 75e6a368-a50c-4736-98ef-4ece99e88c19;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 18694ff4-cffa-4b5c-ae1b-534a9e6d5983;
						- _myState = 8192;
						- _name = "validateEvent";
						- _objectCreation = "32570111735202520-21935753";
						- _umlDependencyID = "3037";
						- m_szSequence = "7.";
						- m_szActualArgs = "newEventInfo";
						- m_szReturnVal = "eventInfoValidated";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 94afbbd3-8ff0-4a37-a158-c2ac27d16af6;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 94afbbd3-8ff0-4a37-a158-c2ac27d16af6;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "validateEvent()";
							- _id = GUID 1ce6ffb2-2c1c-425e-b6b3-5a00732117b2;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- ExecutionOccurrences = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IExecutionOccurrence 
						- _id = GUID f1415668-6dfc-45ae-9197-76447732c223;
						- _objectCreation = "32570131735202520-21935953";
						- _umlDependencyID = "1685";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID b424c1f8-5d4d-41c2-b9b3-5bf18f1f876b;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 478;
					}
					{ IExecutionOccurrence 
						- _id = GUID 44d005d1-8bf9-48d0-8103-b897f3d185d7;
						- _objectCreation = "32570151735202520-21936153";
						- _umlDependencyID = "1680";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID e7317f97-6a4d-4e50-a030-b9602fbb8c2b;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 276;
					}
				}
				- CombinedFragments = { IRPYRawContainer 
					- size = 3;
					- value = 
					{ ICombinedFragment 
						- _id = GUID d84c194d-97a9-4ccf-b5b5-6f203b31d1bf;
						- _myState = 2048;
						- _name = "interactionOperator_0";
						- _objectCreation = "32570171735202520-21936353";
						- _umlDependencyID = "3855";
						- _interactionOperator = "opt";
						- InteractionOperands = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IInteractionOperand 
								- _id = GUID 95df5a2f-5590-4fa9-8c8d-bdac520a47b8;
								- _myState = 2048;
								- _name = "interactionOperand_0";
								- _objectCreation = "32570191735202520-21936553";
								- _umlDependencyID = "3728";
								- _interactionConstraint = "eventType==\"group\"";
							}
						}
					}
					{ ICombinedFragment 
						- _id = GUID c1d69640-da38-434c-a3c9-1c71fcb38b68;
						- _myState = 2048;
						- _name = "interactionOperator_1";
						- _objectCreation = "32570211735202520-21936753";
						- _umlDependencyID = "3855";
						- _interactionOperator = "opt";
						- InteractionOperands = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IInteractionOperand 
								- _id = GUID 68d98946-22ce-402c-aec8-982d15280512;
								- _myState = 2048;
								- _name = "interactionOperand_0";
								- _objectCreation = "32570231735202520-21936953";
								- _umlDependencyID = "3727";
								- _interactionConstraint = "User.accountType==\"manager\"&
eventCreatorID=User.uID";
							}
						}
					}
					{ ICombinedFragment 
						- _id = GUID 8be8ebfa-6f2e-4772-81f1-b213fd764644;
						- _myState = 2048;
						- _name = "interactionOperator_2";
						- _objectCreation = "32570251735202520-21937153";
						- _umlDependencyID = "3855";
						- _interactionOperator = "opt";
						- InteractionOperands = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IInteractionOperand 
								- _id = GUID edfff77c-30cf-4432-8299-6899ccaf7e07;
								- _myState = 2048;
								- _name = "interactionOperand_0";
								- _objectCreation = "32570271735202520-21937353";
								- _umlDependencyID = "3726";
								- _interactionConstraint = "eventInfoValidated==True";
							}
						}
					}
				}
			}
		}
		{ IMSC 
			- _id = GUID cf3184a7-1688-42aa-bf65-e660b63aaaa8;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 6;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "CombinedFragment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,250,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "ControlFlow";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InstanceLine";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,96,437";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InteractionOperand";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,100,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Fill.Transparent_Fill";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Message";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "execution_occurrence";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "SequenceDiagram";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "General";
								- Properties = { IRPYRawContainer 
									- size = 3;
									- value = 
									{ IProperty 
										- _Name = "ClassCentricMode";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "CleanupRealized";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "RealizeMessages";
										- _Value = "True";
										- _Type = Bool;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Log In";
			- _objectCreation = "32570291735202520-21937553";
			- _umlDependencyID = "2163";
			- _lastModifiedTime = "4.27.2025::1:29:28";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 20;
				- m_usingActivationBar = 0;
				- _id = GUID ac683e93-d915-46c1-b2c9-035a95ac7da5;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IMSC";
					- _id = GUID cf3184a7-1688-42aa-bf65-e660b63aaaa8;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 13;
				{ CGIBox 
					- _id = GUID f2a98035-ac7a-4817-ad2e-bf40fabf5cc8;
					- m_type = 108;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID 5e61c0ea-1620-463b-bd9d-66b9623aa2e7;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "opt";
					- _id = GUID 9ee72db3-cdd6-4cd9-9e0a-92107465061d;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID 833ec954-1057-4dd6-8b76-cfdbbaff9027;
					}
					- m_pParent = GUID f2a98035-ac7a-4817-ad2e-bf40fabf5cc8;
					- m_name = { CGIText 
						- m_str = "interactionOperator_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 0 178 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 348 168  348 268  794 268  794 168  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=100>
<frame Id=GUID 87149ecc-095c-4a13-81fb-4c207e947038>";
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "opt";
					- _id = GUID 24fc9dce-7eef-4fbc-a732-b8e0a07d26ca;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID a180f776-68e1-41af-aca0-eb930a8cce00;
					}
					- m_pParent = GUID f2a98035-ac7a-4817-ad2e-bf40fabf5cc8;
					- m_name = { CGIText 
						- m_str = "interactionOperator_1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 0 204 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 348 288  348 392  794 392  794 288  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=104>
<frame Id=GUID 23a5d29b-9f96-46ea-bc1a-0ed424378558>";
				}
				{ CGIMscColumnCR 
					- _id = GUID 154098b1-4659-4d1e-9388-00e537b9a8cd;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 024397bf-b677-43c6-9030-9d20c0f21c40;
					}
					- m_pParent = GUID f2a98035-ac7a-4817-ad2e-bf40fabf5cc8;
					- m_name = { CGIText 
						- m_str = ":User";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0129498 372 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID efeb55f7-0d71-45c5-ace0-4bb9a0b1219a;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID a43631b4-33d4-47e0-9ddc-2571e3d6be2a;
					}
					- m_pParent = GUID 154098b1-4659-4d1e-9388-00e537b9a8cd;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 892.334 42 8494.34 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID cf78fdd1-45ac-42a4-a8b9-d916cfe36466;
				}
				{ CGIMscMessage 
					- _id = GUID a16501f7-fc4c-44ad-b391-3e228ea4e585;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID a74fc299-af97-46d6-9c57-d544edfcba43;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "User.accountType=getAccountTypeFromDB(User.username)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -133 -8  262 -8  262 10  -133 10  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 1;
						- m_transform = 1.00759 0 0 1 562.01 459 ;
						- m_nHorizontalSpacing = 2;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 154098b1-4659-4d1e-9388-00e537b9a8cd;
					- m_sourceType = 'F';
					- m_pTarget = GUID 154098b1-4659-4d1e-9388-00e537b9a8cd;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 450 534  450 570  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 37375 ;
					- m_TargetPort = 48 40155 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 8c0d302d-4b26-4c7c-93e5-156ad599b9d6;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 65b503f0-d288-47d6-b536-5d74da253d3e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "storedUserPass=getPasswordFromDB(User.username)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 154098b1-4659-4d1e-9388-00e537b9a8cd;
					- m_sourceType = 'F';
					- m_pTarget = GUID 154098b1-4659-4d1e-9388-00e537b9a8cd;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 450 388  450 427  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 26101 ;
					- m_TargetPort = 48 29112 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID cf78fdd1-45ac-42a4-a8b9-d916cfe36466;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 94c6068f-0007-42aa-972c-03c16e9f2f71;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "logIn(username, password)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 154098b1-4659-4d1e-9388-00e537b9a8cd;
					- m_sourceType = 'F';
					- m_pTarget = GUID 154098b1-4659-4d1e-9388-00e537b9a8cd;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 450 131  450 160  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 6255 ;
					- m_TargetPort = 48 8494 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID efeb55f7-0d71-45c5-ace0-4bb9a0b1219a;
				}
				{ CGIMscMessage 
					- _id = GUID d010e78b-d392-46db-9397-58d288cd2f92;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID b1053f75-39a2-487a-bb3f-04e8bf9667e6;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "usernameExists=checkUsernameExistsInDB(User.username)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 154098b1-4659-4d1e-9388-00e537b9a8cd;
					- m_sourceType = 'F';
					- m_pTarget = GUID 154098b1-4659-4d1e-9388-00e537b9a8cd;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 448 301  448 326  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 19383 ;
					- m_TargetPort = 48 21313 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID f4c158b1-f96e-4bb5-9253-b6fc7327c389;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 1fc3dbd5-849f-4091-855b-a4e779eebcae;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "User.username=setUsername(username)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 154098b1-4659-4d1e-9388-00e537b9a8cd;
					- m_sourceType = 'F';
					- m_pTarget = GUID 154098b1-4659-4d1e-9388-00e537b9a8cd;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 444 190  444 217  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 10811 ;
					- m_TargetPort = 48 12896 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 0c054df0-cb68-47ac-bb9b-24caede716d7;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 182d45a2-5cef-4e16-9557-cb25155e2e15;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "User.password=setPassword(password)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 154098b1-4659-4d1e-9388-00e537b9a8cd;
					- m_sourceType = 'F';
					- m_pTarget = GUID 154098b1-4659-4d1e-9388-00e537b9a8cd;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 449 244  449 270  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 14981 ;
					- m_TargetPort = 48 16989 ;
					- m_bLeft = 0;
				}
				{ CGIMscInteractionOperand 
					- _id = GUID 87149ecc-095c-4a13-81fb-4c207e947038;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID b6784c5f-d274-4371-853e-09329d101574;
					}
					- m_pParent = GUID 9ee72db3-cdd6-4cd9-9e0a-92107465061d;
					- m_name = { CGIText 
						- m_str = "usernameExists==True";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 348 168  794 168  794 268  348 268  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIMscInteractionOperand 
					- _id = GUID 23a5d29b-9f96-46ea-bc1a-0ed424378558;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID 4e904c0c-9ae7-4f80-86ac-c05f5a4c09b5;
					}
					- m_pParent = GUID 24fc9dce-7eef-4fbc-a732-b8e0a07d26ca;
					- m_name = { CGIText 
						- m_str = "storedUserPass==User.password";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 348 288  794 288  794 392  348 392  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID f2a98035-ac7a-4817-ad2e-bf40fabf5cc8;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID 8ab0fde4-735d-49e2-ba05-80f58a789e9c;
			}
			- m_pICollaboration = { ICollaboration 
				- _id = GUID 5e61c0ea-1620-463b-bd9d-66b9623aa2e7;
				- _objectCreation = "32570311735202520-21937753";
				- _umlDependencyID = "1685";
				- ClassifierRoles = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IClassifierRole 
						- _id = GUID 024397bf-b677-43c6-9030-9d20c0f21c40;
						- _myState = 2048;
						- _objectCreation = "32570331735202520-21937953";
						- _umlDependencyID = "1689";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "User";
							- _id = GUID 4cf3efd0-6e29-483e-8429-ddf6e1f309e8;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- Messages = { IRPYRawContainer 
					- size = 6;
					- value = 
					{ IMessage 
						- _id = GUID 65b503f0-d288-47d6-b536-5d74da253d3e;
						- _myState = 8192;
						- _name = "getPasswordFromDB";
						- _objectCreation = "32570351735202520-21938153";
						- _umlDependencyID = "3393";
						- m_szSequence = "5.";
						- m_szActualArgs = "User.username";
						- m_szReturnVal = "storedUserPass";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 024397bf-b677-43c6-9030-9d20c0f21c40;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 024397bf-b677-43c6-9030-9d20c0f21c40;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "getPasswordFromDB()";
							- _id = GUID e1d6d8b7-0536-47c3-8fc5-b32ae8f75951;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID b1053f75-39a2-487a-bb3f-04e8bf9667e6;
						- _myState = 8192;
						- _name = "checkUsernameExistsInDB";
						- _objectCreation = "32570371735202520-21938353";
						- _umlDependencyID = "3987";
						- m_szSequence = "4.";
						- m_szActualArgs = "User.username";
						- m_szReturnVal = "usernameExists";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 024397bf-b677-43c6-9030-9d20c0f21c40;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 024397bf-b677-43c6-9030-9d20c0f21c40;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "checkUsernameExistsInDB()";
							- _id = GUID 4d42e0b6-d086-46e0-ad32-0416903ad3d2;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID a74fc299-af97-46d6-9c57-d544edfcba43;
						- _myState = 8192;
						- _name = "getAccountTypeFromDB";
						- _objectCreation = "32570391735202520-21938553";
						- _umlDependencyID = "3685";
						- m_szSequence = "6.";
						- m_szActualArgs = "User.username";
						- m_szReturnVal = "User.accountType";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 024397bf-b677-43c6-9030-9d20c0f21c40;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 024397bf-b677-43c6-9030-9d20c0f21c40;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "getAccountTypeFromDB()";
							- _id = GUID 359c513e-e8b4-4fc1-a986-178a6efd0fe8;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 94c6068f-0007-42aa-972c-03c16e9f2f71;
						- _myState = 8192;
						- _name = "logIn";
						- _objectCreation = "32570411735202520-21938753";
						- _umlDependencyID = "2192";
						- m_szSequence = "1.";
						- m_szActualArgs = "username, password";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 024397bf-b677-43c6-9030-9d20c0f21c40;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 024397bf-b677-43c6-9030-9d20c0f21c40;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "logIn()";
							- _id = GUID eb0a1af8-3eab-4921-a68e-bb6d3a4becdf;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID a43631b4-33d4-47e0-9ddc-2571e3d6be2a;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 1fc3dbd5-849f-4091-855b-a4e779eebcae;
						- _myState = 8192;
						- _name = "setUsername";
						- _objectCreation = "32570431735202520-21938953";
						- _umlDependencyID = "2855";
						- m_szSequence = "2.";
						- m_szActualArgs = "username";
						- m_szReturnVal = "User.username";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 024397bf-b677-43c6-9030-9d20c0f21c40;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 024397bf-b677-43c6-9030-9d20c0f21c40;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "setUsername()";
							- _id = GUID 9c75681e-3cb5-4008-b080-03bc6ed1b8b6;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 182d45a2-5cef-4e16-9557-cb25155e2e15;
						- _myState = 8192;
						- _name = "setPassword";
						- _objectCreation = "32570451735202520-21939153";
						- _umlDependencyID = "2869";
						- m_szSequence = "3.";
						- m_szActualArgs = "password";
						- m_szReturnVal = "User.password";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 024397bf-b677-43c6-9030-9d20c0f21c40;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 024397bf-b677-43c6-9030-9d20c0f21c40;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "setPassword()";
							- _id = GUID 44900e2b-d5fa-4ec6-b9f6-3557549488ef;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- ExecutionOccurrences = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IExecutionOccurrence 
						- _id = GUID a43631b4-33d4-47e0-9ddc-2571e3d6be2a;
						- _objectCreation = "32570471735202520-21939353";
						- _umlDependencyID = "1690";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 94c6068f-0007-42aa-972c-03c16e9f2f71;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 416;
					}
				}
				- CombinedFragments = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ ICombinedFragment 
						- _id = GUID 833ec954-1057-4dd6-8b76-cfdbbaff9027;
						- _myState = 2048;
						- _name = "interactionOperator_0";
						- _objectCreation = "32570491735202520-21939553";
						- _umlDependencyID = "3865";
						- _interactionOperator = "opt";
						- InteractionOperands = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IInteractionOperand 
								- _id = GUID b6784c5f-d274-4371-853e-09329d101574;
								- _myState = 2048;
								- _name = "interactionOperand_0";
								- _objectCreation = "32570511735202520-21939753";
								- _umlDependencyID = "3729";
								- _interactionConstraint = "usernameExists==True";
							}
						}
					}
					{ ICombinedFragment 
						- _id = GUID a180f776-68e1-41af-aca0-eb930a8cce00;
						- _myState = 2048;
						- _name = "interactionOperator_1";
						- _objectCreation = "32570531735202520-21939953";
						- _umlDependencyID = "3865";
						- _interactionOperator = "opt";
						- InteractionOperands = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IInteractionOperand 
								- _id = GUID 4e904c0c-9ae7-4f80-86ac-c05f5a4c09b5;
								- _myState = 2048;
								- _name = "interactionOperand_0";
								- _objectCreation = "32570551735202520-21940153";
								- _umlDependencyID = "3719";
								- _interactionConstraint = "storedUserPass==User.password";
							}
						}
					}
				}
			}
		}
		{ IMSC 
			- _id = GUID aaae194e-68b2-4c1f-b606-17a56b298ba1;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 5;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "CombinedFragment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,250,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InstanceLine";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,96,437";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InteractionOperand";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,100,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Fill.Transparent_Fill";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Message";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "execution_occurrence";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "SequenceDiagram";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "General";
								- Properties = { IRPYRawContainer 
									- size = 3;
									- value = 
									{ IProperty 
										- _Name = "ClassCentricMode";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "CleanupRealized";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "RealizeMessages";
										- _Value = "True";
										- _Type = Bool;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Create Account";
			- _objectCreation = "32570571735202520-21940353";
			- _umlDependencyID = "2996";
			- _lastModifiedTime = "4.27.2025::1:33:34";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 20;
				- m_usingActivationBar = 0;
				- _id = GUID 6ce0692a-d193-4b54-a687-73ccac720a80;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IMSC";
					- _id = GUID aaae194e-68b2-4c1f-b606-17a56b298ba1;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 8;
				{ CGIBox 
					- _id = GUID 8fe675b0-ff32-4d3c-88f5-aadfde0d6b71;
					- m_type = 108;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID f50f937a-26a2-49f1-97c6-864134905ecd;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "opt";
					- _id = GUID aa27da5f-0e5a-41e8-a7a4-baf38df4b1d7;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID 961cd5ed-f266-42e5-89c7-473afcf4a83a;
					}
					- m_pParent = GUID 8fe675b0-ff32-4d3c-88f5-aadfde0d6b71;
					- m_name = { CGIText 
						- m_str = "interactionOperator_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 611 228  611 333  940 333  940 228  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=105>
<frame Id=GUID d33ef1b5-262b-4a28-a054-7d421939be2f>";
				}
				{ CGIMscColumnCR 
					- _id = GUID 021ae41e-1b59-4179-9ebd-efc862279ff8;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID aadc381a-17cc-44d7-868d-f26355e1f1bd;
					}
					- m_pParent = GUID 8fe675b0-ff32-4d3c-88f5-aadfde0d6b71;
					- m_name = { CGIText 
						- m_str = ":User";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.00767766 604 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 770c6862-e348-441c-b226-b28f1d11df90;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID bd13dc43-e4a3-48d7-b7ec-765e906b4b64;
					}
					- m_pParent = GUID 021ae41e-1b59-4179-9ebd-efc862279ff8;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 575.262 42 13936.5 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 8c8fcd90-3b69-496d-984a-050a86e487fd;
				}
				{ CGIMscMessage 
					- _id = GUID 4f8c6b0a-957c-4cad-8db8-1556ec4f6c0e;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID f6828fda-2c8e-4c20-bd01-3202237fd7ec;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "passwordConfirmed=confirmPassword(password, confirmPassword)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 021ae41e-1b59-4179-9ebd-efc862279ff8;
					- m_sourceType = 'F';
					- m_pTarget = GUID 021ae41e-1b59-4179-9ebd-efc862279ff8;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 682 179  682 211  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 16802 ;
					- m_TargetPort = 48 20970 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 8c8fcd90-3b69-496d-984a-050a86e487fd;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 50db65ab-8637-4951-b004-53f5ccedab74;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "createAccount(username, password, confirmPassword)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 021ae41e-1b59-4179-9ebd-efc862279ff8;
					- m_sourceType = 'F';
					- m_pTarget = GUID 021ae41e-1b59-4179-9ebd-efc862279ff8;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 682 130  682 157  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 10420 ;
					- m_TargetPort = 48 13937 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 770c6862-e348-441c-b226-b28f1d11df90;
				}
				{ CGIMscMessage 
					- _id = GUID fcfd9354-49a0-4403-9fa1-70a02e2fe301;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 2738a05a-da46-4746-9be4-21cc2a552c89;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "addCredentialsToDB(username, password)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 021ae41e-1b59-4179-9ebd-efc862279ff8;
					- m_sourceType = 'F';
					- m_pTarget = GUID 021ae41e-1b59-4179-9ebd-efc862279ff8;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 682 267  682 301  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 28264 ;
					- m_TargetPort = 48 32692 ;
					- m_bLeft = 0;
				}
				{ CGIMscInteractionOperand 
					- _id = GUID d33ef1b5-262b-4a28-a054-7d421939be2f;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID 3414edc3-0f3f-443e-b883-03f20e58c403;
					}
					- m_pParent = GUID aa27da5f-0e5a-41e8-a7a4-baf38df4b1d7;
					- m_name = { CGIText 
						- m_str = "passwordConfirmed";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 611 228  940 228  940 333  611 333  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 8fe675b0-ff32-4d3c-88f5-aadfde0d6b71;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID 8ab0fde4-735d-49e2-ba05-80f58a789e9c;
			}
			- m_pICollaboration = { ICollaboration 
				- _id = GUID f50f937a-26a2-49f1-97c6-864134905ecd;
				- _objectCreation = "32570591735202520-21940553";
				- _umlDependencyID = "1687";
				- ClassifierRoles = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IClassifierRole 
						- _id = GUID aadc381a-17cc-44d7-868d-f26355e1f1bd;
						- _myState = 2048;
						- _objectCreation = "32570611735202520-21940753";
						- _umlDependencyID = "1682";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "User";
							- _id = GUID 4cf3efd0-6e29-483e-8429-ddf6e1f309e8;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- Messages = { IRPYRawContainer 
					- size = 3;
					- value = 
					{ IMessage 
						- _id = GUID 50db65ab-8637-4951-b004-53f5ccedab74;
						- _myState = 8192;
						- _name = "createAccount";
						- _objectCreation = "32570631735202520-21940953";
						- _umlDependencyID = "3031";
						- m_szSequence = "1.";
						- m_szActualArgs = "username, password, confirmPassword";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID aadc381a-17cc-44d7-868d-f26355e1f1bd;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID aadc381a-17cc-44d7-868d-f26355e1f1bd;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "createAccount()";
							- _id = GUID 78220f29-573c-485d-9e1b-8cfcef06ab18;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID bd13dc43-e4a3-48d7-b7ec-765e906b4b64;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID f6828fda-2c8e-4c20-bd01-3202237fd7ec;
						- _myState = 8192;
						- _name = "confirmPassword";
						- _objectCreation = "32570651735202520-21941153";
						- _umlDependencyID = "3282";
						- m_szSequence = "2.";
						- m_szActualArgs = "password, confirmPassword";
						- m_szReturnVal = "passwordConfirmed";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID aadc381a-17cc-44d7-868d-f26355e1f1bd;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID aadc381a-17cc-44d7-868d-f26355e1f1bd;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "confirmPassword()";
							- _id = GUID b10c8c58-5caf-407e-a749-53813178ae11;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 2738a05a-da46-4746-9be4-21cc2a552c89;
						- _myState = 8192;
						- _name = "addCredentialsToDB";
						- _objectCreation = "32570671735202520-21941353";
						- _umlDependencyID = "3445";
						- m_szSequence = "3.";
						- m_szActualArgs = "username, password";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID aadc381a-17cc-44d7-868d-f26355e1f1bd;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID aadc381a-17cc-44d7-868d-f26355e1f1bd;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "User";
							- _name = "addCredentialsToDB()";
							- _id = GUID abdfb474-fee8-4aaf-a9d6-cf1f893b812d;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- ExecutionOccurrences = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IExecutionOccurrence 
						- _id = GUID bd13dc43-e4a3-48d7-b7ec-765e906b4b64;
						- _objectCreation = "32570691735202520-21941553";
						- _umlDependencyID = "1689";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 50db65ab-8637-4951-b004-53f5ccedab74;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 159;
					}
				}
				- CombinedFragments = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ ICombinedFragment 
						- _id = GUID 961cd5ed-f266-42e5-89c7-473afcf4a83a;
						- _myState = 2048;
						- _name = "interactionOperator_0";
						- _objectCreation = "32570711735202520-21941753";
						- _umlDependencyID = "3855";
						- _interactionOperator = "opt";
						- InteractionOperands = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IInteractionOperand 
								- _id = GUID 3414edc3-0f3f-443e-b883-03f20e58c403;
								- _myState = 2048;
								- _name = "interactionOperand_0";
								- _objectCreation = "32570731735202520-21941953";
								- _umlDependencyID = "3728";
								- _interactionConstraint = "passwordConfirmed";
							}
						}
					}
				}
			}
		}
	}
	- Components = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IComponent 
			- fileName = "DefaultComponent";
			- _id = GUID eb8cc07c-afdf-48cd-a213-09a012030068;
		}
	}
	- UCDiagrams = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IUCDiagram 
			- _id = GUID a88a39b7-e9f2-433c-9fb4-b48ad12daac2;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 5;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Actor";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,26,84,168";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "111,0,107";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Association";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "ControlFlow";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "System_Border";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,228,240";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "111,0,107";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "UseCase";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,21,129,92";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "111,0,107";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Use Case Diagram";
			- _objectCreation = "32570751735202520-21942153";
			- _umlDependencyID = "3057";
			- _lastModifiedTime = "5.15.2025::1:24:42";
			- _graphicChart = { CGIClassChart 
				- _id = GUID d50f1f9f-cbfd-4dac-889c-7e2b6b6f18ed;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IUCDiagram";
					- _id = GUID a88a39b7-e9f2-433c-9fb4-b48ad12daac2;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 27;
				{ CGIClass 
					- _id = GUID ffa3c48e-f811-4109-88ea-977455fad1ed;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID 40c63d4c-48a3-4efa-b80b-c395387a36d3;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIBox 
					- _id = GUID cb71b711-f3e9-46d0-b144-10fac481cd85;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 123;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID ffa3c48e-f811-4109-88ea-977455fad1ed;
					- m_name = { CGIText 
						- m_str = "Calendar";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.35342 0 0 0.57258 366 105 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 1240  1228 1240  1228 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 5999c1ce-78b9-49e2-9d90-4bc2b16e422c;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Add Event";
						- _id = GUID af9e2121-7a79-4406-b0be-c4e231412ae1;
					}
					- m_pParent = GUID cb71b711-f3e9-46d0-b144-10fac481cd85;
					- m_name = { CGIText 
						- m_str = "Add Event";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.393553 0 0 0.11578 403.5 101.412 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 2d535f8f-de3a-4a07-a554-fb98a268fbe8;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Delete Event";
						- _id = GUID fc40b0c6-bd49-404e-9ed4-a916be487c5a;
					}
					- m_pParent = GUID cb71b711-f3e9-46d0-b144-10fac481cd85;
					- m_name = { CGIText 
						- m_str = "Delete Event";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.393553 0 0 0.11578 395.628 246.369 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID f9d4a23e-3ede-4b00-a7db-090a1c97211f;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Edit Event";
						- _id = GUID 352cfde1-681e-41b4-a006-2a6855473f46;
					}
					- m_pParent = GUID cb71b711-f3e9-46d0-b144-10fac481cd85;
					- m_name = { CGIText 
						- m_str = "Edit Event";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.393553 0 0 0.11578 397.841 393.073 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 75fd35a9-af3d-4e14-8721-9878f872652e;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "View Event";
						- _id = GUID 2caa0271-dea1-4713-ace4-0381f93373f6;
					}
					- m_pParent = GUID cb71b711-f3e9-46d0-b144-10fac481cd85;
					- m_name = { CGIText 
						- m_str = "View Event";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.393553 0 0 0.11578 397.841 531.045 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 37ca3986-217b-4c79-91fe-331d432a9c78;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "View Monthly-Based List";
						- _id = GUID 25eb2e33-8069-4955-802a-30b6e3a719d3;
					}
					- m_pParent = GUID cb71b711-f3e9-46d0-b144-10fac481cd85;
					- m_name = { CGIText 
						- m_str = "View Monthly-Based List";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.393553 0 0 0.11578 398.457 677.75 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID c72ca423-e553-40a7-b8d9-a8b7d34c1e94;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Coordinate Meeting";
						- _id = GUID 9acbf824-5fbf-4706-b484-bc1e5b6a48dd;
					}
					- m_pParent = GUID cb71b711-f3e9-46d0-b144-10fac481cd85;
					- m_name = { CGIText 
						- m_str = "Coordinate Meeting";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.393553 0 0 0.11578 406.329 1100.4 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 7b66acdc-c676-41a9-a026-faba5d269987;
					- m_type = 124;
					- m_pModelObject = { IHandle 
						- _m2Class = "IActor";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "UserActor";
						- _id = GUID 0852bf81-659a-48b9-b2b2-59b31c067ed0;
					}
					- m_pParent = GUID ffa3c48e-f811-4109-88ea-977455fad1ed;
					- m_name = { CGIText 
						- m_str = "UserActor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.077634 0 0 0.123909 199.895 348.023 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 40 250  40 1396  1122 1396  1122 250  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIAssociationEnd 
					- _id = GUID 3c2a466b-75ee-4b95-9884-1bf3eb0b860e;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "UserActor";
						- _name = "itsAdd Event";
						- _id = GUID 0caea654-c6ff-43a9-9599-457cdef584b2;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 7b66acdc-c676-41a9-a026-faba5d269987;
					- m_sourceType = 'F';
					- m_pTarget = GUID 5999c1ce-78b9-49e2-9d90-4bc2b16e422c;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 542 363 ;
					- m_TargetPort = 111 783 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Add Event";
						- _name = "itsUserActor";
						- _id = GUID f02f5492-ec54-47c1-be29-9ed2e8a400eb;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID ef6ba68b-ec80-4979-b053-f31ec640fb17;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "UserActor";
						- _name = "itsDelete Event";
						- _id = GUID 46c64cdf-6673-481c-9c0d-1c052cfcdc84;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 7b66acdc-c676-41a9-a026-faba5d269987;
					- m_sourceType = 'F';
					- m_pTarget = GUID 2d535f8f-de3a-4a07-a554-fb98a268fbe8;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 980 524 ;
					- m_TargetPort = 131 738 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Delete Event";
						- _name = "itsUserActor";
						- _id = GUID cbbe53f7-b170-400a-8ce7-1e44cc555925;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID 88a1cce7-a11f-4796-b8f4-89a7d51ab76b;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "UserActor";
						- _name = "itsEdit Event";
						- _id = GUID e290589f-c59f-4ed3-84ad-0be72b393c0b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 7b66acdc-c676-41a9-a026-faba5d269987;
					- m_sourceType = 'F';
					- m_pTarget = GUID f9d4a23e-3ede-4b00-a7db-090a1c97211f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 542 791 ;
					- m_TargetPort = 882 753 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Edit Event";
						- _name = "itsUserActor";
						- _id = GUID 632c1297-284c-4485-bf7a-b948ba640c20;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID 4bc53891-d108-4f0b-b16d-68bfc6f80d23;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "UserActor";
						- _name = "itsView Event";
						- _id = GUID 25a2c834-103a-4fbf-8932-b78da60f55dd;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 7b66acdc-c676-41a9-a026-faba5d269987;
					- m_sourceType = 'F';
					- m_pTarget = GUID 75fd35a9-af3d-4e14-8721-9878f872652e;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 748 944 ;
					- m_TargetPort = 1022 693 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "View Event";
						- _name = "itsUserActor";
						- _id = GUID f68d123d-78fa-4440-9d7d-67dcb45f04e0;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID 83da05a8-4ef9-4a1d-835a-6db3bbb9ac36;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "UserActor";
						- _name = "itsView Monthly-Based List";
						- _id = GUID 26bc5189-8f83-46d2-a539-56e84639a7fa;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 7b66acdc-c676-41a9-a026-faba5d269987;
					- m_sourceType = 'F';
					- m_pTarget = GUID 37ca3986-217b-4c79-91fe-331d432a9c78;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 748 1057 ;
					- m_TargetPort = 707 557 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "View Monthly-Based List";
						- _name = "itsUserActor";
						- _id = GUID 718afdd8-24bd-4fa2-ba76-38fc19c5cc50;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIBasicClass 
					- _id = GUID cfe5d4b8-d8fd-4bbd-9172-65e9948153bd;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Log In";
						- _id = GUID f0be27f3-597b-44e9-81a1-d6dfaee78863;
					}
					- m_pParent = GUID cb71b711-f3e9-46d0-b144-10fac481cd85;
					- m_name = { CGIText 
						- m_str = "Log In";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.385954 0 0 0.11578 405.39 822.711 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIAssociationEnd 
					- _id = GUID 2bdc937c-d6c1-412f-8b4e-01643443e1e5;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "UserActor";
						- _name = "itsLog In";
						- _id = GUID 019f2bf7-c11f-42e1-afdb-5a107cd20377;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 7b66acdc-c676-41a9-a026-faba5d269987;
					- m_sourceType = 'F';
					- m_pTarget = GUID cfe5d4b8-d8fd-4bbd-9172-65e9948153bd;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 903 1275 ;
					- m_TargetPort = 174 497 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Log In";
						- _name = "itsUserActor";
						- _id = GUID f9c66f55-d182-492a-a7c9-2bbab7bac88e;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIBasicClass 
					- _id = GUID 5d2d593b-2641-4880-a48a-a18393c959bf;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Create account";
						- _id = GUID 1af61a05-9e72-483a-9348-8b57223d7d97;
					}
					- m_pParent = GUID cb71b711-f3e9-46d0-b144-10fac481cd85;
					- m_name = { CGIText 
						- m_str = "Create account";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.368411 0 0 0.11578 411.014 958.931 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIAssociationEnd 
					- _id = GUID ea7d1f55-8b4d-4696-a734-bef27e688d35;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "UserActor";
						- _name = "itsCreate account";
						- _id = GUID 80c306f4-fa27-4cf6-a4c5-40148d16ef80;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 7b66acdc-c676-41a9-a026-faba5d269987;
					- m_sourceType = 'F';
					- m_pTarget = GUID 5d2d593b-2641-4880-a48a-a18393c959bf;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 929 1364 ;
					- m_TargetPort = 167 557 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Create account";
						- _name = "itsUserActor";
						- _id = GUID 12ddb825-505f-4fbc-8670-95202ef8fa95;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIBasicClass 
					- _id = GUID d629ceb5-d9ef-4dee-9dc5-ce97815f4a50;
					- m_type = 124;
					- m_pModelObject = { IHandle 
						- _m2Class = "IActor";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "ManagerActor";
						- _id = GUID a59bbdce-f0ad-49ef-9425-4e27c66e1eba;
					}
					- m_pParent = GUID ffa3c48e-f811-4109-88ea-977455fad1ed;
					- m_name = { CGIText 
						- m_str = "ManagerActor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.077634 0 0 0.123909 931.895 333.023 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 40 250  40 1396  1122 1396  1122 250  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIAssociationEnd 
					- _id = GUID 767b82e4-2750-40f4-a1c9-925a17d27932;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "ManagerActor";
						- _name = "itsAdd Event_1";
						- _id = GUID edf51e92-dc97-4e4c-b7ea-4aadd4081b4d;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID d629ceb5-d9ef-4dee-9dc5-ce97815f4a50;
					- m_sourceType = 'F';
					- m_pTarget = GUID 5999c1ce-78b9-49e2-9d90-4bc2b16e422c;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 581 710 ;
					- m_TargetPort = 844 557 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Add Event";
						- _name = "itsManagerActor_1";
						- _id = GUID 3ef357cd-af5f-4597-ae13-c3aa765d5ad0;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID 15ffd385-eb34-46b6-8758-a63df23efd52;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "ManagerActor";
						- _name = "itsDelete Event_1";
						- _id = GUID 6f0c1a4b-c979-48c9-8626-43c6efedced4;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID d629ceb5-d9ef-4dee-9dc5-ce97815f4a50;
					- m_sourceType = 'F';
					- m_pTarget = GUID 2d535f8f-de3a-4a07-a554-fb98a268fbe8;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 542 799 ;
					- m_TargetPort = 986 587 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Delete Event";
						- _name = "itsManagerActor_1";
						- _id = GUID 528faea1-d06e-46ce-89b3-36705abfeecb;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID f49942a7-41da-4eab-a74e-61ae21e2482d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "ManagerActor";
						- _name = "itsEdit Event_1";
						- _id = GUID 78a09c14-1705-48d4-8367-388e269f2468;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID d629ceb5-d9ef-4dee-9dc5-ce97815f4a50;
					- m_sourceType = 'F';
					- m_pTarget = GUID f9d4a23e-3ede-4b00-a7db-090a1c97211f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 465 904 ;
					- m_TargetPort = 923 527 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Edit Event";
						- _name = "itsManagerActor_1";
						- _id = GUID 84eff044-de45-4116-8ec7-5cc66c81a6cb;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID 6c3cae03-42fd-49be-bed1-8ecda66d5d02;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "ManagerActor";
						- _name = "itsView Event_1";
						- _id = GUID f7691069-1495-4829-8f7c-255d78e59df0;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID d629ceb5-d9ef-4dee-9dc5-ce97815f4a50;
					- m_sourceType = 'F';
					- m_pTarget = GUID 75fd35a9-af3d-4e14-8721-9878f872652e;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 426 1041 ;
					- m_TargetPort = 902 331 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "View Event";
						- _name = "itsManagerActor_1";
						- _id = GUID 1400da2e-05d1-45ee-b717-a1c0370dd5b9;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID 770fc4e1-95aa-46ea-83b1-9716d60084f0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "ManagerActor";
						- _name = "itsView Monthly-Based List_1";
						- _id = GUID 1da311ce-e5e8-4aab-82b0-2b5b0fdbafd3;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID d629ceb5-d9ef-4dee-9dc5-ce97815f4a50;
					- m_sourceType = 'F';
					- m_pTarget = GUID 37ca3986-217b-4c79-91fe-331d432a9c78;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 362 1097 ;
					- m_TargetPort = 893 542 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "View Monthly-Based List";
						- _name = "itsManagerActor_1";
						- _id = GUID 9b142867-8291-43c4-96a7-8e170cdc1322;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID c34ce65e-dca0-46f2-9ac0-9f3acf756204;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "ManagerActor";
						- _name = "itsLog In";
						- _id = GUID c8ec679c-46cc-468a-aec3-abef69645662;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID d629ceb5-d9ef-4dee-9dc5-ce97815f4a50;
					- m_sourceType = 'F';
					- m_pTarget = GUID cfe5d4b8-d8fd-4bbd-9172-65e9948153bd;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 401 1138 ;
					- m_TargetPort = 724 376 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Log In";
						- _name = "itsManagerActor";
						- _id = GUID 9f5a96ce-45b1-4721-b918-09f2808bddd1;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID 0fddbdd7-a2d3-4c89-b168-6c5bedf677cb;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "ManagerActor";
						- _name = "itsCreate account";
						- _id = GUID f84bc06f-742a-4e78-ac04-bafb77c01a34;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID d629ceb5-d9ef-4dee-9dc5-ce97815f4a50;
					- m_sourceType = 'F';
					- m_pTarget = GUID 5d2d593b-2641-4880-a48a-a18393c959bf;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 220 1283 ;
					- m_TargetPort = 927 391 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Create account";
						- _name = "itsManagerActor";
						- _id = GUID 24c91fb5-0b9a-485b-b191-fddcd453b296;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID 2cb06719-2b62-4935-872a-f1567d5633b1;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "ManagerActor";
						- _name = "itsCoordinate Meeting_1";
						- _id = GUID bb8303af-0969-4a87-ae23-2564a59e82fd;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID d629ceb5-d9ef-4dee-9dc5-ce97815f4a50;
					- m_sourceType = 'F';
					- m_pTarget = GUID c72ca423-e553-40a7-b8d9-a8b7d34c1e94;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 207 1340 ;
					- m_TargetPort = 1053 467 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Coordinate Meeting";
						- _name = "itsManagerActor_1";
						- _id = GUID 37efac0f-60a6-4e50-b10f-04ec1237df1c;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID ffa3c48e-f811-4109-88ea-977455fad1ed;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID 8ab0fde4-735d-49e2-ba05-80f58a789e9c;
			}
		}
	}
}

