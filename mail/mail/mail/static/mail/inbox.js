document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
 
  document.querySelector('form').onsubmit = send_email;

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#single-email-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function reply(recipient , subject, timestamp, body) {
  document.querySelector('.reply').addEventListener('click', () => {
    // Show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#single-email-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';

   // Pre-fill values
    let subjectPreFill = '';
    if (subject.startsWith('Re: ')) {
      subjectPreFill = `${subject}`
    } else {
      subjectPreFill = `Re: ${subject}`
    }
   

    document.querySelector('#compose-recipients').value = recipient;
    document.querySelector('#compose-subject').value = subjectPreFill;
    document.querySelector('#compose-body').value = `\n\n\n----- On ${timestamp} ${recipient} wrote:\n\n${body}`;
  });
}
function send_email() {
 
   recipients = document.querySelector('#compose-recipients').value;
   subject = document.querySelector('#compose-subject').value;
   body = document.querySelector('#compose-body').value;
 
    // Post email to API route
    fetch('/emails' , {
      method: 'POST',
      body: JSON.stringify({
        recipients: recipients,
        subject: subject,
        body: body
  
      })
    })
    .then(response => response.json())
    .then(result => {
      // Print result
      console.log(result);
      load_mailbox('sent');
      alert(result.message);
 
    });
    
    localStorage.clear();   
    
    return false;
  
 }

function load_mailbox(mailbox) {
 
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#single-email-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  
  // Show the mailbox name
  // document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`
 
   
    
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>
  <table style="width:100%"><thead><tr><th>The State</th><th>Sender</th><th>Subject</th><th>Date and Time</th></tr></thead></table>`;
  if(mailbox === "sent") {
    document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>
  <table style="width:100%"><thead><tr><th>The State</th><th>Recipient</th><th>Subject</th><th>Date and Time</th></tr></thead></table>`;
  }


   const table = document.querySelector('table');
  
   const tbody = document.createElement('tbody');
  
  
  // thead.append(tr);
  // table.append(thead);
   table.append(tbody);


  // Load emails

  //fetch('/emails/inbox')
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
      // Print emails
     // console.log(emails);
      

  if (emails.length === 0){
      tbody.innerHTML = `
      <tr>
        <td colspan='3' class="alert alert-warning text-center" role="alert">
          The mailbox is empty.
        </td>
      </tr>`;
    }
    else
    {
      emails.forEach(email => {
         
          tr = document.createElement("tr");
          tr.dataset.page = email.id;
        
 
         // tr.setAttribute('data-page', email.id);
           tr.setAttribute('class', 'email-link');
          
          if (mailbox === "sent")
          {
            tr.innerHTML = `<td data-page="${email.id}"class="email-link">
            <i class="far fa-envelope"></i>  </td>
            <td data-page="${email.id}"class="email-link"> ${email.recipients} </td>
            <td data-page="${email.id}"class="email-link"> ${email.subject} </td>            
            <td data-page="${email.id}"class="email-link"> ${email.timestamp} </td>`
          }
          if (mailbox === "inbox" || mailbox === "archive")
          {
            if (email.read){
              tr.setAttribute('class' , 'email-read')
              tr.innerHTML = `<td data-page="${email.id}"class="email-link">
              <i class="far fa-envelope-open"></i></td>
              <td data-page="${email.id}"class="email-link"> ${email.sender} </td>
              <td data-page="${email.id}"class="email-link"> ${email.subject} </td>
              <td data-page="${email.id}"class="email-link"> ${email.timestamp} </td>
              <td data-page="${email.id}"class="unarchive_bin alt"> <i class="fas fa-undo"></i>
              <span class="alttext">unrchive</span> </td>`
            }
            else
            {
              tr.setAttribute('class', 'email-unread');
              tr.innerHTML = `<td data-page="${email.id}"class="email-link">
              <i class="far fa-envelope"></i> </td>
              <td data-page="${email.id}"class="email-link"> ${email.sender} </td>
              <td data-page="${email.id}"class="email-link"> ${email.subject} </td>
              <td data-page="${email.id}"class="email-link"> ${email.timestamp} </td>
              <td data-page="${email.id}"class="unarchive_bin alt"> <i class="fa fa-undo" aria-hidden="true"></i><span class="alttext">Unarchive</span> </td>`
            }
              if (mailbox === "inbox" || mailbox === "archive") {
                if (email.archived)
                {
                  tr.setAttribute('class', 'archive');
                  tr.innerHTML = `<td data-page="${email.id}"class="email-link">
                  <i class="far fa-envelope-open"></i>  </td>
                  <td data-page="${email.id}"class="email-link"> ${email.sender} </td>
                  <td data-page="${email.id}"class="email-link"> ${email.subject} </td>
                  <td data-page="${email.id}"class="email-link"> ${email.timestamp} </td>
                  <td data-page="${email.id}"class="archive_bin alt"> <i class="fas fa-archive"></i>
                  <span class="alttext">Archived</span> </td>`
                } 
              }
          }            
          tbody.appendChild(tr);
          view_email();
       });
      }
         // table.appendChild(tbody);
          
          return false;
  });
  

}


function view_email(email_id) {
    document.querySelector('tbody').addEventListener('click', (e) => {
      const email_id = e.target.parentElement.dataset.page;
      document.querySelector('#emails-view').style.display = 'none';
      document.querySelector('#single-email-view').style.display = 'block';
      document.querySelector('#compose-view').style.display = 'none';

      const view = document.querySelector('#emails-view');
      const mailbox = view.firstChild.innerHTML.toLowerCase();
      
      
    
      fetch(`/emails/${email_id}`)
        .then(response => response.json())
        .then(email => {
          //console.log(email);
      

      document.querySelector('h5').innerHTML = email.subject; 
      view.innerHTML = `<div class='view-mail-container' data-id=${email_id}></div>` 
      const viewMail = document.querySelector('.view-mail-container');
      const emailDiv = document.createElement('div');
      emailDiv.id= "email";
      emailDiv.className = "row";
      viewMail.append(emailDiv);
         
      document.querySelector('.view-mail-archive').innerHTML =  `${ mailbox !== 'sent' ? 
              `<button type="button" class="btn btn-warning archive-btn">
              <i class="fas fa-archive"></i>&nbsp; ${email.archived ? '<span class="archive">Unarchive</span>': '<span class="archive">Archive</span>' }</button>`: '' }
            <button type="button" class="btn btn-success reply"><i class="fas fa-reply"></i>&nbsp; Reply</button>`;

      document.querySelector('#sender').innerHTML = email.sender;
      document.querySelector('#recipients').innerHTML = email.recipients;
      document.querySelector('#timestamp').innerHTML = email.timestamp;


      document.querySelector('#mail-body').innerHTML = email.body;

           // Mark email as read
      if (mailbox === 'inbox'){
          mark_email_as_read(email_id);
        }

        // Reply to an email
        reply(email.sender, email.subject, email.timestamp, email.body)
       
        // Mark email as archived
        if (mailbox === 'inbox' || mailbox === 'archive'){
  
          archive()
        }

  });

   });
}

function mark_email_as_read(email_id) {  
  console.log(`updating email as read = true`);
  fetch(`/emails/${email_id}`, {
    method: 'PUT',
    body: body = JSON.stringify({
      read: true
    })
  })
}

function archive() {
  const viewMail = document.querySelector('.view-mail-container');
  const archiveBtn = document.querySelector('.archive-btn');
  const archive = document.querySelector('.archive');
  const emailId = viewMail.dataset.id;

  archiveBtn.addEventListener('click', () => {
    let onOff = true;
    if (archive.textContent === 'Archive') {
      onOff = true;
    } else {
      onOff = false;
    }

    fetch(`/emails/${emailId}`, {
      method: 'PUT',
      body: JSON.stringify({
        archived: onOff
      })
    }).then(() => {
      load_mailbox('inbox')
    })
  });
  
}
