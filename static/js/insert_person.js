function submit_insert_person(){
	//if ($('#add_person').attr('value')=='Cadastrar'){action='submit';}else{action ='update';}
	var information = '';
	var full_name = $('#full_name').val();
	var email = $('#email').val();
	var cellphone = $('#cellphone').val();
	var birth_date = $('#birth_date').val();
	var keypoints = $('#keypoints').val();

	information = '&full_name='+full_name+'&email=='+email+'&cellphone='+cellphone+' &birth_date= '+
		birth_date+'&keypoints='+keypoints;
	alert(information);
	document.getElementById("submit_form").submit();
}