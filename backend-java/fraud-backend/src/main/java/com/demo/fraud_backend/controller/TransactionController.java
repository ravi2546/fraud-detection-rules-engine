package com.demo.fraud_backend.controller;

import java.util.Map;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import com.demo.fraud_backend.dto.TransactionRequest;

@RestController
@RequestMapping("/api/transaction")
public class TransactionController {

    @PostMapping
    public ResponseEntity<?> process(@RequestBody TransactionRequest request) {

        // Connect to AI Engine
        RestTemplate restTemplate = new RestTemplate();

        ResponseEntity<Map> response =
            restTemplate.postForEntity(
                "http://localhost:8001/check-fraud",
                request,
                Map.class
            );

        // Return AI Engine response
        return ResponseEntity.ok(response.getBody());
    }
}
