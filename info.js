document.addEventListener('DOMContentLoaded', function () {
    const bookingInfo = JSON.parse(localStorage.getItem('bookingInfo'));
    if (bookingInfo) {
        const infoDiv = document.getElementById('bookingInfo');
        infoDiv.innerHTML = `
        <h2>Booking Details</h2>
        <p><strong>Name</strong><span>:</span> <span  class="Content">${bookingInfo.name}</span></p>
        <p><strong>Mobile Number</strong><span>:</span> <span class="Content">${bookingInfo.mobileNumber}</span></p>
        <p><strong>Check-in Date</strong><span>:</span> <span class="Content">${bookingInfo.checkInDate}</span></p>
        <p><strong>Number of Nights</strong><span>:</span> <span class="Content">${bookingInfo.numNights}</span></p>
        <p><strong>Additional Persons</strong><span>:</span> <span class="Content">${bookingInfo.numPersons}</span></p>
        <p><strong>Selected Room</strong><span>:</span> <span class="Content">${bookingInfo.selectedRoom}</span></p>
        <p><strong>Selected Amenities</strong><span>:</span> <span class="Content">${bookingInfo.selectedAmenities.join(', ')}</span></p>
        <p><strong>Advance Payment</strong><span>:</span> <span class="Content">${bookingInfo.advancePayment}</span></p>
        <p><strong>Total Room Cost</strong><span>:</span> <span class="Content">${bookingInfo.totalRoomCost}</span></p>
        <p><strong>Total Amenities Cost</strong><span>:</span> <span class="Content">${bookingInfo.totalAmenitiesCost}</span></p>
        <p><strong>Total Cost</strong><span>:</span> <span class="Content">${bookingInfo.totalCost}</span></p>
        <p><strong>Balance Amount</strong><span>:</span> <span class="Content">${bookingInfo.balanceAmount}</span></p>
        `;
    }
});


