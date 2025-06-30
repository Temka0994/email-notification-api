CREATE TABLE users(
    user_id BIGSERIAL PRIMARY KEY,
    email VARCHAR(80) UNIQUE,
    password TEXT
);


CREATE TABLE notifications (
    notification_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES users(user_id) ON DELETE CASCADE,
    to_email VARCHAR(80) NOT NULL,
    subject VARCHAR(80) NOT NULL,
    message TEXT NOT NULL,
    scheduled_at TIMESTAMP WITH TIME ZONE NOT NULL,
    status BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);