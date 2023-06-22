$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					translate(v = [0, 0, 0]) {
						rotate(a = [0, 0, 0]) {
							linear_extrude(height = 8) {
								text(font = "DejaVu Sans Mono:style=Bold", halign = "center", size = 17, text = "OMER", valign = "center");
							}
						}
					}
					translate(v = [0, 0, 0.5000000000]) {
						rotate(a = [0, 0, 0]) {
							linear_extrude(height = 7.5000000000) {
								offset(r = -0.5000000000) {
									text(font = "DejaVu Sans Mono:style=Bold", halign = "center", size = 17, text = "OMER", valign = "center");
								}
							}
						}
					}
				}
			}
		}
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				hull() {
					translate(v = [-36.0000000000, 9.7500000000, 0]) {
						rotate(a = [0, 0, 0]) {
							translate(v = [0, 0, 0]) {
								rotate(a = [0, 0, 0]) {
									cylinder(h = 0.5000000000, r = 1);
								}
							}
						}
					}
					translate(v = [36.0000000000, 9.7500000000, 0]) {
						rotate(a = [0, 0, 0]) {
							translate(v = [0, 0, 0]) {
								rotate(a = [0, 0, 0]) {
									cylinder(h = 0.5000000000, r = 1);
								}
							}
						}
					}
					translate(v = [-36.0000000000, -9.7500000000, 0]) {
						rotate(a = [0, 0, 0]) {
							translate(v = [0, 0, 0]) {
								rotate(a = [0, 0, 0]) {
									cylinder(h = 0.5000000000, r = 1);
								}
							}
						}
					}
					translate(v = [36.0000000000, -9.7500000000, 0]) {
						rotate(a = [0, 0, 0]) {
							translate(v = [0, 0, 0]) {
								rotate(a = [0, 0, 0]) {
									cylinder(h = 0.5000000000, r = 1);
								}
							}
						}
					}
				}
			}
		}
	}
	union() {
		#translate(v = [33.7500000000, 7.5000000000, -50]) {
			rotate(a = [0, 0, 0]) {
				cylinder(h = 100, r = 1.8000000000);
			}
		}
		#translate(v = [33.7500000000, 0, -50]) {
			rotate(a = [0, 0, 0]) {
				cylinder(h = 100, r = 1.8000000000);
			}
		}
		#translate(v = [33.7500000000, -7.5000000000, -50]) {
			rotate(a = [0, 0, 0]) {
				cylinder(h = 100, r = 1.8000000000);
			}
		}
		#translate(v = [-33.7500000000, 7.5000000000, -50]) {
			rotate(a = [0, 0, 0]) {
				cylinder(h = 100, r = 1.8000000000);
			}
		}
		#translate(v = [-33.7500000000, 0, -50]) {
			rotate(a = [0, 0, 0]) {
				cylinder(h = 100, r = 1.8000000000);
			}
		}
		#translate(v = [-33.7500000000, -7.5000000000, -50]) {
			rotate(a = [0, 0, 0]) {
				cylinder(h = 100, r = 1.8000000000);
			}
		}
	}
}