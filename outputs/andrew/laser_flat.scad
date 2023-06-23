$fn = 50;


union() {
	translate(v = [0, 0, 0]) {
		projection() {
			intersection() {
				translate(v = [-500, -500, 1.5000000000]) {
					cube(size = [1000, 1000, 0.1000000000]);
				}
				difference() {
					union() {
						translate(v = [0, 10.5000000000, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									translate(v = [0, 0, 0]) {
										rotate(a = [0, 0, 0]) {
											linear_extrude(height = 8) {
												text(font = "DejaVu Sans Mono:style=Bold", halign = "center", size = 13, text = "ANDR-", valign = "center");
											}
										}
									}
									translate(v = [0, 0, 0.5000000000]) {
										rotate(a = [0, 0, 0]) {
											linear_extrude(height = 7.5000000000) {
												offset(r = -0.5000000000) {
													text(font = "DejaVu Sans Mono:style=Bold", halign = "center", size = 13, text = "ANDR-", valign = "center");
												}
											}
										}
									}
								}
							}
						}
						translate(v = [0, -10.5000000000, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									translate(v = [0, 0, 0]) {
										rotate(a = [0, 0, 0]) {
											linear_extrude(height = 8) {
												text(font = "DejaVu Sans Mono:style=Bold", halign = "center", size = 13, text = "EW", valign = "center");
											}
										}
									}
									translate(v = [0, 0, 0.5000000000]) {
										rotate(a = [0, 0, 0]) {
											linear_extrude(height = 7.5000000000) {
												offset(r = -0.5000000000) {
													text(font = "DejaVu Sans Mono:style=Bold", halign = "center", size = 13, text = "EW", valign = "center");
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
									translate(v = [-32.0000000000, 17.0000000000, 0]) {
										rotate(a = [0, 0, 0]) {
											translate(v = [0, 0, 0]) {
												rotate(a = [0, 0, 0]) {
													cylinder(h = 0.5000000000, r = 5);
												}
											}
										}
									}
									translate(v = [32.0000000000, 17.0000000000, 0]) {
										rotate(a = [0, 0, 0]) {
											translate(v = [0, 0, 0]) {
												rotate(a = [0, 0, 0]) {
													cylinder(h = 0.5000000000, r = 5);
												}
											}
										}
									}
									translate(v = [-32.0000000000, -17.0000000000, 0]) {
										rotate(a = [0, 0, 0]) {
											translate(v = [0, 0, 0]) {
												rotate(a = [0, 0, 0]) {
													cylinder(h = 0.5000000000, r = 5);
												}
											}
										}
									}
									translate(v = [32.0000000000, -17.0000000000, 0]) {
										rotate(a = [0, 0, 0]) {
											translate(v = [0, 0, 0]) {
												rotate(a = [0, 0, 0]) {
													cylinder(h = 0.5000000000, r = 5);
												}
											}
										}
									}
								}
							}
						}
					}
					union() {
						translate(v = [-30.0000000000, -15.0000000000, -125.0000000000]) {
							rotate(a = [0, 0, 0]) {
								cylinder(h = 250, r = 1.5000000000);
							}
						}
						translate(v = [-30.0000000000, 0.0000000000, -125.0000000000]) {
							rotate(a = [0, 0, 0]) {
								cylinder(h = 250, r = 1.5000000000);
							}
						}
						translate(v = [-30.0000000000, 15.0000000000, -125.0000000000]) {
							rotate(a = [0, 0, 0]) {
								cylinder(h = 250, r = 1.5000000000);
							}
						}
						translate(v = [30.0000000000, -15.0000000000, -125.0000000000]) {
							rotate(a = [0, 0, 0]) {
								cylinder(h = 250, r = 1.5000000000);
							}
						}
						translate(v = [30.0000000000, 0.0000000000, -125.0000000000]) {
							rotate(a = [0, 0, 0]) {
								cylinder(h = 250, r = 1.5000000000);
							}
						}
						translate(v = [30.0000000000, 15.0000000000, -125.0000000000]) {
							rotate(a = [0, 0, 0]) {
								cylinder(h = 250, r = 1.5000000000);
							}
						}
					}
				}
			}
		}
	}
}