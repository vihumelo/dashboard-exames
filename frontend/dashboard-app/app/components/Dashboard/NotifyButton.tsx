import { Button } from "antd";
import React, { useState } from "react";
import axios from "axios";

interface NotifyButtonProps {
  itemId: number;
  onSuccess: () => void;
}

const NotifyButton: React.FC<NotifyButtonProps> = ({ itemId, onSuccess }) => {
  const [isNotifying, setIsNotifying] = useState(false);

  const handleNotify = async () => {
    try {
      setIsNotifying(true);

      await axios.post("http://127.0.0.1:8000/notify/", {
        id: itemId,
      });

      onSuccess();
    } catch (error) {
      console.error("Erro ao notificar:", error);
      window.alert("Erro ao notificar");
    } finally {
      setIsNotifying(false);
    }
  };

  return (
    <Button
      type="primary"
      className="notify-button"
      onClick={handleNotify}
      loading={isNotifying}
    >
      Notificar
    </Button>
  );
};

export default NotifyButton;
